#!/usr/bin/env python3
import tkinter
from tkinter import ttk
import datetime as dt
import time
import PIL.Image
from tkinter import *
import os

LARGE_FONT= ("Nexa Light", 12)


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
        else:
            self.label['text']="Good Evening!"


        
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
           litsen_button=ttk.Button(self, text="Litsen",command=self.butler)
           litsen_button.pack()
    def salutations(self):
        a= dt.datetime.now().strftime('%H')
        a=int(a)
        if a < 12:
            self.label['text']="Good Morning!"
        else:
            self.label['text']="Good Evening!"
        
    def butler(self):
        import speech_recognition as sr
        r=sr.Recognizer()
        with sr.Microphone() as source:
            self.label['text']="Speak out Your Command!"
            audio=r.listen(source)

        try:
            self.label['text']=r.recognize_google(audio)
        except sr.UnknownValueError:
            self.label['text']="Sorry i cant understand you!"
        except sr.RequestError as e:
            self.label['text']=e
        #self.butler()
        
        
            
            
        
        
        
            
            
  


app=GuiInit()
app.mainloop()
