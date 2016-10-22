#!/usr/bin/env python3
import tkinter
from tkinter import ttk
import datetime as dt
import time

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
        for F in (XavierFace, me, Home):
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
            



app=GuiInit()
app.mainloop()
