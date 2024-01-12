import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol] -= quantity

    def get_stock_price(self, symbol):
        api_url = f"https://www.alphavantage.co/query"
        function = "GLOBAL_QUOTE"
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        if "Global Quote" in data:
            return float(data["Global Quote"]["05. price"])
        else:
            return None

    def track_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                total_value += price * quantity

        return total_value

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
    api_key = 'YOUR_API_KEY'
    
    portfolio_tracker = StockPortfolio(api_key)

    # Add stocks to the portfolio
    portfolio_tracker.add_stock("AAPL", 5)
    portfolio_tracker.add_stock("GOOGL", 3)
    portfolio_tracker.add_stock("MSFT", 8)

    # Remove some stocks from the portfolio
    portfolio_tracker.remove_stock("AAPL", 2)

    # Track and display the portfolio value
    total_value = portfolio_tracker.track_portfolio_value()
    print(f"Total Portfolio Value: ${total_value:.2f}")
