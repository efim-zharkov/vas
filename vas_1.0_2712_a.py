import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, Idk what the hell is this.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

def main():
    speak("Hello, how can I assist you today?")
    while True:
        command = listen()
        if command:
            if "hello" in command.lower():
                speak("Hello!")

            elif 'weather' in command.lower():
                webbrowser.open("https://www.accuweather.com/en/gr/thessaloniki/186405/weather-forecast/186405")

            elif 'open youtube' in command.lower():
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in command.lower():
                webbrowser.open("https://www.google.com")

            elif 'open chat' in command.lower():
                webbrowser.open("https://discord.com/channels/@me")

            elif 'play some music' in command.lower():
                webbrowser.open("https://open.spotify.com/")
                speak("Ok, here is some music for you")

            elif 'thank you' in command.lower():
                speak("You are welcome!")

            elif "goodbye" in command.lower():
                speak("Goodbye!")
                break

            else:
                speak("Sorry, Idk what the hell is this.")

if __name__ == "__main__":
    main()
