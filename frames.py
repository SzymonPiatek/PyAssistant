from settings import *
from widgets import *

import tkinter as tk
import customtkinter as ctk

import speech_recognition as sr
import nltk
from nltk.corpus import wordnet
import pyttsx3
import pyaudio
import webbrowser
import time

class Assistant(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master = master, fg_color = COLOR)

        # create widgets
        self.assistant_button = FirstButton(self, text = START, func = self.start)

        # display widgets
        self.assistant_button.place(relx = 0.5, rely = 0.5, anchor = 'center',
                               relwidth = 0.3, relheight = 0.3)
            
    def speak(self, text, rate = 120):
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()

    def recognize_speech(self):
        recognizer = sr.Recognizer()
            
        with sr.Microphone() as source:
            text = HELP
            self.assistant_button.configure(text = text)
            self.speak(text)
            audio = recognizer.listen(source, timeout = 3)

        try:
            text = recognizer.recognize_google(audio)
            return text
        
        except sr.UnknownValueError:
            text = NO_UNDERSTAND
            self.assistant_button.configure(text = text)
            self.speak(text)
            return ''

    def open_in_google_chrome(url):
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)

    def recognize_command(self, user_input):
        google_chrome = ['open google chrome', 'open google', 'open chrome', 'google chrome', 'google', 'chrome']
        youtube = ['open youtube', 'youtube']
        facebook = ['open facebook', 'facebook']

        if user_input in google_chrome:
            self.speak('I open Google Chrome')
            self.open_in_google_chrome(url = '')
        elif user_input in youtube:
            self.speak('I open Youtube in Google Chrome')
            self.open_in_google_chrome(url = 'youtube.com')
        elif user_input in facebook:
            self.speak('I open Facebook in Google Chrome')
            self.open_in_google_chrome(url = 'facebook.com')

    def start(self):
        if wordnet:
            pass
        else:
            nltk.download('wordnet')

        user_input = (self.recognize_speech()).lower()

        self.assistant_button.configure(text = ('You said:', user_input))
        self.recognize_command(user_input)