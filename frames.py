from settings import *
from widgets import *

import tkinter as tk
import customtkinter as ctk

import sys

import speech_recognition as sr
import nltk
from nltk.corpus import wordnet
import pyttsx3
import webbrowser
import pywhatkit

class Assistant(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master = master, fg_color = COLOR)

        # create widgets
        self.assistant_button = FirstButton(self, text = START, func = self.start)
        self.assistant_label = FirstLabel(self, text = '🙂')

        # display widgets
        self.assistant_button.place(relx = 0.5, rely = 0.8, anchor = 'center',
                               relwidth = 0.6, relheight = 0.1)
        self.assistant_label.place(relx = 0.5, rely = 0.35, anchor = 'center')

    def speak(self, text, rate = 130):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('pitch', 1)

        self.engine.say(text)
        self.engine.runAndWait()

    def recognize_speech(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            text = HELP
            self.assistant_button.configure(text = text)
            self.assistant_label.configure(text = '🧐')
            self.update()
            self.speak(text)
            self.assistant_button.configure(text = LISTEN)
            self.update()
            audio = recognizer.listen(source, timeout = 3)

        try:
            text = recognizer.recognize_google(audio)
            return text
        
        except sr.UnknownValueError:
            text = NO_UNDERSTAND
            self.assistant_button.configure(text = text)
            self.assistant_label.configure(text = '😑')
            self.update()
            self.speak(text)
            return False

    def open_in_google_chrome(self, url):
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)

    def recognize_command(self, user_input):
        google_chrome = ['open google chrome', 'open google', 'open chrome']
        facebook = ['open facebook', 'facebook']
        messenger = ['open messenger', 'messenger']

        # Youtube
        if 'youtube' in user_input:
            pywhatkit.playonyt(user_input)
            self.speak('I opened Youtube')
        # New chrome tab 
        elif user_input in google_chrome:
            pywhatkit.search('')
        # Facebook
        elif user_input in facebook:
            self.open_in_google_chrome(url = 'facebook.com')
            self.speak('I opened Facebook in Google Chrome')
        # Messenger
        elif user_input in messenger:
            self.open_in_google_chrome(url = 'messenger.com')
            self.speak('I opened Messenger in Google Chrome')
        # Query in Google Chrome
        else:
            pywhatkit.search(user_input)
            self.speak('I opened Google Chrome with this query')
        
        self.assistant_label.configure(text = '😎')
        self.update()

    def start(self):
        if wordnet:
            pass
        else:
            nltk.download('wordnet')

        user_input = self.recognize_speech()
        
        if user_input is not False:
            user_input = user_input.lower()
            self.recognize_command(user_input)
            self.assistant_button.configure(text = START)
            self.update()
        elif user_input is False:
            self.assistant_button.configure(text = START)
            self.update()