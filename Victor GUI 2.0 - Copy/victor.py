import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
from victorui import Ui_victorGUI


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)


# text to speach


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to covert voice into text

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour < 12 and hour > 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Victor at your service sir. How can I help you")


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chootlaha@gmail.com', 'imchoot@007')
    server.sendmail('chootlaha@gmail.com', to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=6, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except:
            speak("Say that again please...")
            # speak("Sorry, I couldn't understand what you said")
            return "none"
        return query

    # to wish

    # to send email

    def TaskExecution(self):
        wish()
        # speak("this is victor at your service")
        # while True:
        while True:

            self.query = self.takecommand().lower()

            # logic building for task

            if "open notepad" in self.query:  # WORKING
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            # elif "open adobe reader" in query:
            #     apath =

            elif "open command prompt" in self.query:  # WORKING
                os.system("start cmd")

            elif "open camera" in self.query:  # WORKING
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('img', img)
                    if cv2.waitKey(1) & 0xff == ord('c'):
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:  # WORKING
                music_dir = "D:\Songs & Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:  # WORKING
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

            elif "wikipedia" in self.query:  # WORKING
                speak("Searching wikipedia.....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:  # WORKING
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:  # WORKING
                webbrowser.open("www.facebook.com")

            elif "open instagram" in self.query:  # WORKING
                webbrowser.open("www.instagram.com")

            elif "open twitter" in self.query:  # WORKING
                webbrowser.open("www.twitter.com")

            elif "google search" in self.query:  # WORKING
                import wikipedia as googlescrap
                self.query = self.query.replace("victor", "")
                self.query = self.query.replace("google search", "")
                self.query = self.query.replace("google", "")
                speak("This is what I found on the web")
                kit.search(self.query)

                try:
                    result = googlescrap.summary(self.query, 2)
                    speak(result)

                except:
                    speak("No data available")

            elif "send whatsapp message" in self.query:  # NOTWORKING
                kit.sendwhatmsg("+919800024338", "this is testing protocol", 5, 11)

            elif "play videos on youtube" in self.query:
                speak("Sir, what video should i play")  # WORKING
                vid = self.takecommand().lower()
                kit.playonyt(f"{vid}")

            elif "send email" in self.query:  # WORKING
                try:
                    speak("What should I say?")
                    content = self.takecommand().lower()
                    speak("Please enter the receiver's mail id: ")
                    to = input("Enter the mail id here:  ")
                    speak("Enter 'Y' to send the mail or 'N' to cancel it")
                    activate = input("Y & N: ").lower()
                    if activate == "y":
                        sendemail(to, content)
                        speak("Email has been sent to the person")
                    else:
                        pass
                except:
                    speak(
                        "Sorry sir, I am not able to sent this mail, please try again later")

            elif "no thanks" in self.query:
                speak("Thanks for using me sir, have a good day ")
                sys.exit()
            elif "shutdown" in self.query:
                speak("Thanks for using me sir, have a good day ")
                sys.exit()
            speak("Sir, do you have any other work")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_victorGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("GIF/tuse.png")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("GIF/round_orig.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("GIF/Jarvis_Loading_Screen.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("GIF/78_04_article.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("GIF/J4o.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)


app = QApplication(sys.argv)
victor = Main()
victor.show()
exit(app.exec_())
