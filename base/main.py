import speech_recognition as sr
import nltk
from nltk.corpus import wordnet
import pyttsx3
import webbrowser

def speak(text, rate = 120):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('How can i help you?')
        audio = recognizer.listen(source, timeout = 3)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print('I do not understand you')
        return ''

def open_in_google_chrome(url):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)

def recognize_command(user_input):
    google_chrome = ['open google chrome', 'open google', 'open chrome', 'google chrome', 'google', 'chrome']
    youtube = ['open youtube', 'youtube']
    facebook = ['open facebook', 'facebook']

    if user_input in google_chrome:
        open_in_google_chrome(url = '')
    elif user_input in youtube:
        open_in_google_chrome(url = 'youtube.com')
    elif user_input in facebook:
        open_in_google_chrome(url = 'facebook.com')

def main():
    nltk.download('wordnet')

    while True:
        user_input = recognize_speech()
        print("Say 'stop' to quit program")

        if user_input.lower() == 'stop':
            break

        print('You said:', user_input.lower())
        recognize_command(user_input.lower())

        response = 'I understood you!'
        speak(response)

        while True:
            again = input('Can I help you again? (y/n): ')
            if again.lower() == 'n':
                exit()
            elif again.lower() != 'y':
                print('Wrong answer')
                continue


if __name__ == '__main__':
    main()