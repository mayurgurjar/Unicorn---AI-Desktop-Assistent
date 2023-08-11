'''Importing the Packages which is required in this project'''

"In This the code for the Graphical User Interface is written"
from UNIGUI120 import Ui_MainWindow

"The pyQt5 is used for the GUi purpose and in this the overall moment of gui is depend on this file"
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType

"Sys module is used to manipulate the different parts of the Python Runtime Environment"
import sys

"OS module is used to used to interacting with the operating system"
import os

"Time module is used to know the time and time related data"
import time

"pygame is used for playing the sound in the project with the help of the mixer component"
from pygame import mixer

"keyboard module is used for generating the keyboard commands in program"
from keyboard import press
from keyboard import  press_and_release
from keyboard import write

"pyautogui is used for applying the mouse and the keyboard command to the project"
import pyautogui

"Key module , where my api key is written"
from key import apikey

"Pyttsx3 module is used for used for converting text to speech the command and make it to speak by the machine"
import pyttsx3

"datetime module is used to know about the date and dtime information"
import datetime

"speech_recognition module is used to take speech commad from the user"
import speech_recognition as sr

"googletrans is us used to translate the text to any other language"
from googletrans import  Translator

"wikipedia is used to fetch some special information from the wikipedia"
import wikipedia

"webbrowser is used to operate the different webpages"
import webbrowser

"openai module is used for fetching the information from the openai database"
import openai

"Through numpy module we can work with the arrays"
import numpy as np


'''The Main code for the execution of the program is written in the Mainthread class'''
chatStr = ""
class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()

    "Through This function the code will run"
    def run(self):
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[0].id)

        "help in speaking the machine"
        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        "uses for the chatting purpose with the machine"
        def chat(query):
            global chatStr
            print(chatStr)
            openai.api_key = apikey
            chatStr += f"Mayur: {query}\nUnicorn: "
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=chatStr,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            speak(response["choices"][0]["text"])
            chatStr += f"{response['choices'][0]['text']}\n"
            return response["choices"][0]["text"]

        "here the apikey is written and the whole work is done with the api key is handled here"
        def ai(prompt):
            openai.api_key = apikey
            text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            text += response["choices"][0]["text"]
            if not os.path.exists("Openai"):
                os.mkdir("Openai")

            with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
                f.write(text)

        "This function wish the user"
        def wishme():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Hello Sir , Good Morning , Good to see you again , Please tell me sir , How may i assist you")
                print("Good Morning")
            elif hour >= 12 and hour < 18:
                speak("Hello Sir , Good afternoon , Good to see you again , Please tell me sir ,  How may i assist you")
                print("Good Afternoon")
            else:
                speak("Hello Sir , Good evening , Good to see you again , Please tell me sir ,  How may i assist you")
                print("Good Evening")

        "it load the mp3 beep sound which is present in the program"
        mixer.init()
        mixer.music.load("ding.mp3")

        "THis function is helping in the taking command"
        def takecommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                mixer.music.play()
                print("Listening...")
                r.pause_threshold = 0.5
                audio = r.listen(source, 0, 5)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said : {query}")
            except Exception as e:
                print(e)
                print("say that again")
                speak("say that again")
                return "None"
            return query

        "this function help in translating the sentence"
        def trans(Text):
            line = str(Text)
            translate = Translator()
            result = translate.translate(line)
            data = result.text
            print(f"You: {data}")
            return data

        "this function can take the user command through mic and execute the command"
        def micexecute():
            query = takecommand()
            data = trans(query)
            return data

        if __name__ == '__main__':
            wishme()
            while True:
                query = takecommand().lower()
                if "wikipedia" in query:
                    speak("searching wikipedia...")
                    query = query.replace("wikipedia ", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wekipidia")
                    print(results)
                    speak(results)
                elif "close wikipedia".lower() in query:
                    speak("closing wikipedia")
                    press_and_release("ctrl+w")
                elif "open youtube".lower() in query:
                    speak("opening youtube")
                    webbrowser.open("youtube.com")
                    query = takecommand()
                elif "close youtube".lower() in query:
                    speak("closing youtube")
                    press_and_release("ctrl+w")
                elif "open Google".lower() in query:
                    speak("opening google")
                    webbrowser.open("google.com")
                elif "close google".lower() in query:
                    speak("closing Google")
                    press_and_release("ctrl+w")
                elif "open Gmail".lower() in query:
                    speak("opening gmail")
                    webbrowser.open("Gmail.com")
                elif "close gmail".lower() in query:
                    speak("closing gmail")
                    press_and_release("ctrl+w")
                elif "open Instagram".lower() in query:
                    speak("opening instagram")
                    webbrowser.open("instagram.com")
                elif "close instagram".lower() in query:
                    speak("closing instagram")
                    press_and_release("ctrl+w")
                elif "open snapchat".lower() in query:
                    speak("Opening snapchat")
                    webbrowser.open("snapchat.com")
                elif "close snapchat".lower() in query:
                    speak("closing snapchat")
                    press_and_release("ctrl+w")
                elif "play music".lower() in query:
                    speak("sir what song should i play ...")
                    webbrowser.open(f"youtube.com")
                elif "stop music".lower() in query:
                    speak("closing music")
                    press_and_release("ctrl+w")
                elif "pragati gupta".lower() in query:
                    speak("Here is the profile of , Pragati Gupta")
                    webbrowser.open("https://www.linkedin.com/in/gpragati807/")
                elif "close pragati profile".lower() in query:
                    speak("closing pragati's profile")
                    press_and_release("ctrl+w")
                elif "lahar soni".lower() in query:
                    speak("Here is the profile of , Lahar soni")
                    webbrowser.open("https://www.linkedin.com/in/lahar-soni-4506aa25a/")
                elif "close lahar profile".lower() in query:
                    speak("closing lahar's profile")
                    press_and_release("ctrl+w")
                elif "Neeraj kalawat".lower() in query:
                    speak("Here is the profile of , Neeraj kalawat")
                    webbrowser.open("https://www.linkedin.com/in/neeraj-kalawat-973575241/")
                elif "close neeraj profile".lower() in query:
                    speak("closing neeraj's profile")
                    press_and_release("ctrl+w")
                elif "Mayur Gurjar".lower() in query:
                    speak("here is the profile of , Mayur Gurjar")
                    webbrowser.open("www.linkedin.com/in/mayur-gurjar-34166823b")
                elif "close mayur profile".lower() in query:
                    speak("closing mayur's profile")
                    press_and_release("ctrl+w")
                elif "time".lower() in query:
                    strtime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strtime}")
                elif "introduction".lower() in query:
                    speak("Hello , i am Unicorn , speed 1 terabyte , setup 1 gegabyte")
                    speak("That's all about my introduction , i don't have a permission to tell you more about me . ")
                    speak("If you want to know more about me , Please ask to my Owner , Mayur . ")
                elif "unicorn Quit".lower() in query:
                    speak("ok , See you again ")
                    speak("Shutting down .")
                    exit()
                elif "reset chat".lower() in query:
                    speak("reseting chat")
                    chatStr = ""
                else:
                    print("Chatting...")
                    chat(query)

"this help is execute the Mainthread class"
startExe = Mainthread()

"In this class the overall code for the GUI is written"
class gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton_1.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    "in this method the code for the different GIF are written which are used in the program"
    def startTask(self):
        self.gui.label1 = QtGui.QMovie("GUI//download.gif")
        self.gui.GUI_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("GUI//Jarvis_Gui (1).gif")
        self.gui.GUI_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("GUI//Earth.gif")
        self.gui.GUI_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("GUI//2fe4f743123363998082c968ca1130c8_w200.gif")
        self.gui.GUI_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("GUI//iron.gif")
        self.gui.GUI_5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie("GUI//loading.gif")
        self.gui.GUI_6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("GUI//57fa9d62d1a1b9fb4be02c2518738508.gif")
        self.gui.GUI_7.setMovie(self.gui.label7)
        self.gui.label7.start()

        self.gui.label8 = QtGui.QMovie("GUI//y80EW4.gif")
        self.gui.GUI_8.setMovie(self.gui.label8)
        self.gui.label8.start()

        startExe.start()


"the execution for the gui is done here"
Guiapp = QApplication(sys.argv)
unicorn_gui = gui_start()
unicorn_gui.show()
exit(Guiapp.exec_())










