import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and synthesis engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define predefined responses
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm fine, thank you!",
    "what's your name": "I'm just a simple voice assistant.",
    "goodbye": "Goodbye! Have a great day!"
}

def listen_and_respond():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("User:", query)

        # Look for predefined responses
        if query in responses:
            response = responses[query]
            print("Assistant:", response)
            speak(response)
        else:
            print("Assistant: Sorry, I didn't understand that.")

    except sr.UnknownValueError:
        print("Assistant: Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Assistant: Could not request results from Google Speech Recognition service; {e}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you?")
    while True:
        listen_and_respond()
