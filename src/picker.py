#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:23:26 2018

@author: hushmans
"""
import tkinter as tk #do gui
import main

class Picker(tk.Frame):

    def __init__(self, parent):
        self.MyParent = parent
        pm=tk.IntVar()
        timeR=tk.IntVar()
        pm.set(25)
        timeR.set(7)

        #Uruchamia symulacje z odpowiednimi parametrami
        def simulation():
            print(pm.get())
            print(timeR.get())
            self.MyParent.destroy()
            main.mainSim(pm.get(),timeR.get())

        self.frame = tk.Frame.__init__(self, parent)
        #tworzy przyciski wyboru i prompty
        def pmset(a):
            pm.set(a)
        def timeRset(a):
            timeR.set(a)

        #Otwiera nowe okno do podawania atrybutow propagacji
        def propagation():
            win = tk.Toplevel(self)

            #Propagacja
            w = tk.StringVar()
            temp = tk.IntVar()
            prec = tk.IntVar()
            smog = tk.IntVar()

            win.prompt3 = tk.Label(win, text="Start a 5h propagation with:", anchor="center")
            win.windPrompt = tk.Label(win, text="Wind[kt](format:05E):")
            win.wind = tk.Entry(win, bd =3, textvariable=w)
            win.tempPrompt = tk.Label(win, text="Temperature[*C]:")
            win.temperature = tk.Entry(win, bd =3, textvariable=temp)
            win.precipPrompt = tk.Label(win, text="Precipitation[mm]:")
            win.precipitation = tk.Entry(win, bd =3, textvariable=prec)
            win.smogPrompt = tk.Label(win, text="Current pm10 level[um/m2]:")
            win.smog = tk.Entry(win, bd = 3, textvariable=smog)

            #Uruchamia propagacje z odpowiednimi atrybutami
            def propagateStart():
                if (win.wind.get() == "" or win.temperature.get()=="" or win.precipitation.get()=="" or win.smog.get()==""):
                    win.destroy()
                    propagation()
                else:
                    w = win.wind.get()
                    temp = int(win.temperature.get())
                    prec = int(win.precipitation.get())
                    smog = int(win.smog.get())
                    print(w)
                    print(temp)
                    print(prec)
                    print(smog)
                    win.destroy()
                    self.MyParent.destroy()
                    #Wywoluje funkcje z main, ktora liczy brakujace dane i uruchamia propagacje
                    main.propagationSim(w, temp, prec, smog)

            win.startProp = tk.Button(win, text="Start propagation", command=propagateStart) #command

            #Umieszcza przyciski i text w oknie
            win.prompt3.pack(fill="x")
            win.windPrompt.pack(side="top")
            win.wind.pack(side="top")
            win.tempPrompt.pack(side="top")
            win.temperature.pack(side="top")
            win.precipPrompt.pack(side="top")
            win.precipitation.pack(side="top")
            win.smogPrompt.pack(side="top")
            win.smog.pack(side="top")
            win.startProp.pack()


        #wybor typu pylow
        pmType = tk.IntVar()
        self.prompt = tk.Label(self, text="Pick a pm type:", anchor="center")
        self.pm10 = tk.Radiobutton(self, text="PM 10", variable=pmType, value=10, command=lambda:pmset(10))
        self.pm25 = tk.Radiobutton(self, text="PM2.5",variable=pmType, value=25, command=lambda:pmset(25))

        #wybor czasu trwania pomiarow
        tim = tk.IntVar()
        self.prompt2 = tk.Label(self, text="Pick a time range:", anchor="center")
        self.hour = tk.Radiobutton(self, text="24h", variable=tim, value=24, command=lambda:timeRset(24))
        self.week = tk.Radiobutton(self, text="Week", variable=tim, value=7, command=lambda:timeRset(7))

        self.start = tk.Button(self, text="Start simulation", command=simulation)

        self.propagate = tk.Button(self, text="Propagation", command=propagation)

        #ustawia elementy w oknie
        self.prompt.pack(side="top", fill="x")
        self.pm10.pack(side="top")
        self.pm25.pack(side="top")

        self.prompt2.pack(fill="x")
        self.hour.pack(side="top")
        self.week.pack(side="top")

        self.start.pack()

        self.propagate.pack(fill="x")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Air Pollution Simulation")
    Picker(root).pack(fill="both", expand=True)
    root.mainloop()
