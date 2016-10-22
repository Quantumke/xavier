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

app=GuiInit()
app.mainloop()
