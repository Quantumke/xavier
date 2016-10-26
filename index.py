#!/usr/bin/env python3
import tkinter
from tkinter import ttk
import datetime as dt
import time
import PIL.Image
from tkinter import *
import os
from os import popen 
LARGE_FONT= ("Nexa Light", 12)
import csv



class GuiInit(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        self.author="Ben Nguru"
        tkinter.Tk.__init__(self, *args, **kwargs)
        container= tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames={}
        for F in (XavierFace, me, Home, About):
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Home)
    def show_frame(self, count):
        frame=self.frames[count]
        frame.tkraise()

class XavierFace(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.FaceFeatures()
    def FaceFeatures(self):
        self.grid(column=1, row=1, sticky='nsew')
        self.status = ttk.LabelFrame(self, text='My Response', height=100)
        self.status.grid(column=0, row=4, columnspan=4, sticky='nesw')

        self.status_label = ttk.Label(self.status, text='',font=LARGE_FONT)
        self.status_label.grid(column=1, row=2)

        ttk.Label(self, text='I am Xavier',font=LARGE_FONT).grid(column=0, row=0,  columnspan=4)
        ttk.Separator(self, orient='horizontal').grid(column=0, row=1, columnspan=4, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
    def salutations(self):
        a= dt.time()
        a=str(a)
        if a =="00:00:00":
            self.status_label['text']="Good Morning!"
        else:
            self.status_label['text']="Good Evening!"
            


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.salutations()
        self.label = ttk.Label(self, text="Xavier says Hi,", font=LARGE_FONT)
        self.label.pack(pady=1,padx=10)

        button1 = ttk.Button(self, text="About Me",
                            command=lambda: controller.show_frame(About))
        button1.pack()

        button2 = ttk.Button(self, text="How can i help",
                            command=lambda: controller.show_frame(me))
        button2.pack()
  
    def salutations(self):
        self.label = ttk.Label(self, text="Hi", font=LARGE_FONT)
        self.responses= ttk.Label(self, text="", font=LARGE_FONT)
        self.label.pack(pady=1,padx=1)
        self.responses.pack(pady=15,padx=15)
        a= dt.datetime.now().strftime('%H')
        a=int(a)
        if a < 12:
            self.label['text']="Good Morning!"
            os.system('say "Good Morning human! i am an artificial intelligence programe made by a mad genius, called Ben" ')

        else:
            self.label['text']="Good Evening!"
            os.system('say "Good Evening human!" ')



        
class About(ttk.Frame):
     def __init__(self, parent, controller):
         ttk.Frame.__init__(self, parent)
         self.label = ttk.Label(self, text="Xavier says Hi,", font=LARGE_FONT)
         self.label.pack(pady=10,padx=10)
         label = ttk.Label(self, text="Xavier is a neualnetwork,", font=LARGE_FONT)
         label.pack(pady=10,padx=100)
         button1 = ttk.Button(self, text="Back Home",
                            command=lambda: controller.show_frame(Home))
         button1.pack()
         
         



            
class me(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.FaceFeatures()
        self.salutations()
    def FaceFeatures(self):
           self.label = ttk.Label(self, text="Hi", font=LARGE_FONT)
           self.responses= ttk.Label(self, text="", font=LARGE_FONT)
           self.label.pack(pady=10,padx=10)
           self.responses.pack(pady=15,padx=15)
           self.litsen_button=ttk.Button(self, text="Litsen",command=self.butler)
           self.litsen_button.pack()
    def salutations(self):
        a= dt.datetime.now().strftime('%H')
        a=int(a)
        if a < 12:
            self.label['text']="Good Morning!,Speak out Your Command!"


        else:
            self.label['text']="Good Evening!,Speak out Your Command!"
        
    def butler(self):
        import subprocess
        from textblob import TextBlob
        subprocess.call(["afplay", "Submarine.aiff"])
        self.label['text']="Litsening .......!"
        import speech_recognition as sr
        r=sr.Recognizer()
        with sr.Microphone() as source:
            self.label['text']="Speak out Your Command!"
            audio=r.listen(source)

        try:
            self.label['text']=r.recognize_google(audio)
            words=TextBlob(r.recognize_google(audio))
            date=dt.datetime.now()
            sentence=r.recognize_google(audio)
            learn=[date, sentence.encode("utf-8")]
            with open('brain.csv', 'w') as f:
                writer=csv.writter(f)
                writer.writerow(['date','sentence'])
                writee.writerows(learn)
            a=words.words
            for i in a:
                if i == "music":
                    os.system('say "playing music!" ')
                    self.musicplayer()
                if i =="remind" and i =="tomorrow":
                    os.system('say "Adding an event to your schedule"" ')
                    self.reminder_tomorrow(a)
                    
        except sr.UnknownValueError:
            self.label['text']="Sorry i cant understand you!"
            os.system('say "Sorry i cant understand you!" ')
        except sr.RequestError as e:
            self.label['text']=e
            os.system('say "Could not esctablish an internet connection" ')
            self.musicplayer()
        #self.butler()
    def musicplayer(self):
        import glob
        import subprocess
        self.litsen_button["text"]="Stop Music"
        self.litsen_button["width"]=10
        a=glob.glob("/Users/macuser/Desktop/d\'s/*.mp3")
        #sound_program="/Users/macuser/Desktop/Google\ Chrome.app "
        for i in a:
            sound_program="/Users/macuser/Desktop/c.app"
            subprocess.call([sound_program, i])
    def remider_tomorrow(self,a):
        from datetime import datetime
        from threading import Timer
        from xavier.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
        x=datetime.today()
        y=x.replace(day=x.day+1,hour=10,minute=0, second=0,microsecond=0)
        delta_t=y-x
        secs=delta_t.seconds+1
        def send_notifaction():
            username="benmburu"
            phone_number=0721799582
            api_key="5302d778bb12c134db669118414d4598baa91ffc6023f0ce2f34246ffbf10a06"
            to=phone_number
            message="You asked xavier to remind you {0}".format(a)
            gateway = AfricasTalkingGateway(username, api_key)
            results = gateway.sendMessage(to, message)
            t=Timer(secs,send_notifaction)
            t.start()
            os.system('say "added remider" ')
            

        
            
            
        
        
        
            
            
  


app=GuiInit()
app.mainloop()
