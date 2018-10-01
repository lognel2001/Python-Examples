from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

import time
import calendar
import datetime
h = 0
m = 0
s = 0
t = "AM"

def current_time():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24

    #set the time zone
    current_hour = current_hour - 6

    if current_hour>=12:
        tag="PM"
    else:
        tag="AM"
    a = str(h)+":"+str(m)+":"+str(s)+t
    timex = str(current_hour)+":"+str(current_minutes)+":"+str(current_seconds)+tag
    if timex == a:
        beep()
    return timex

x=current_time()
print(x)

def beep():
    winsound.Beep(540,8000)

def quit(*args):
    root.destroy()
    
def show_time():
    global h
    global m
    global s
    global t
    
    time = current_time()
    txt.set(time)
    root.after(1000, show_time)

def get_alarm(*args):
    global h
    h = input("set hour")
    global m
    m = input("set min")
    global s
    s = input("set sec")
    global t
    t = input("am or pm").upper()
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='Blue')
root.bind("x", quit)
root.after(1000, show_time)
fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="Yellow", background="Red")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()




#freq = 440
#winsound.Beep(freq,duration)

##winsound.Beep(480,200)
##
##winsound.Beep(1568,200)
##
##winsound.Beep(1568,200)
##
##winsound.Beep(1568,200)
##
##
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##
##winsound.Beep(369.99,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(369.99,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(392,400)
##
##winsound.Beep(196,400)
##
##
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(83.99,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(830.61,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(987.77,400)
##
##
##winsound.Beep(880,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(830.61,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(987.77,400)
##
##Sleep(200)
##
##winsound.Beep(1108,10)
##winsound.Beep(1174.7,200)
##winsound.Beep(1480,10)
##winsound.Beep(1568,200)
##
##
##Sleep(200)
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(830.61,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(987.77,400)
##
##
##winsound.Beep(880,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(698.46,200)
##
##
##
##winsound.Beep(659.25,200)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(784,200)
##
##winsound.Beep(880,400)
##
##winsound.Beep(784,200)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(659.25,200)
##    
##
##
##winsound.Beep(587.33,200)
##
##winsound.Beep(659.25,200)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(784,400)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(659.25,200)
##
##winsound.Beep(587.33,200)
##
##
##
##winsound.Beep(523.25,200)
##
##winsound.Beep(587.33,200)
##
##winsound.Beep(659.25,200)
##
##winsound.Beep(698.46,400)
##
##winsound.Beep(659.25,200)
##
##winsound.Beep(587.33,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(523.25,200)
##
##
##Sleep(400)
##winsound.Beep(349.23,400)
##
##winsound.Beep(392,200)
##
##winsound.Beep(329.63,200)
##
##winsound.Beep(523.25,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(466.16,200)
##
##
##
##winsound.Beep(440,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(523.25,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(1760,200)
##
##winsound.Beep(440,200)
##
##
##
##winsound.Beep(392,200)
##
##winsound.Beep(440,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(440, 200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(1568,200)
##
##winsound.Beep(392,200)
##
##
##
##winsound.Beep(349.23,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(440,200)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(415.2,200)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(1396.92,200)
##
##winsound.Beep(349.23,200)
##
##
##
##winsound.Beep(329.63,200)
##
##winsound.Beep(311.13,200)
##
##winsound.Beep(329.63,200)
##
##winsound.Beep(659.25,200)
##
##winsound.Beep(698.46,400)
##
##winsound.Beep(783.99,400)
##
##
##
##winsound.Beep(440,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(523.25,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(880,200)
##
##winsound.Beep(1760,200)
##
##winsound.Beep(440,200)
##
##
##
##winsound.Beep(392,200)
##
##winsound.Beep(440,200)
##
##winsound.Beep(493.88,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(440,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(1568,200)
##
##winsound.Beep(392,200)
##
##
##
##winsound.Beep(349.23,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(440,00)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(659.25,200)
##
##winsound.Beep(698.46,200)
##
##winsound.Beep(739.99,200)
##
##winsound.Beep(783.99,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(392,200)
##
##winsound.Beep(196,200)
##
##winsound.Beep(196,200)
##
##winsound.Beep(196,200)
##
##
##
##winsound.Beep(185,200)
##
##winsound.Beep(196,200)
##    
##winsound.Beep(185,200)
##
##winsound.Beep(196,200)
##
##winsound.Beep(207.65,200)
##
##winsound.Beep(220,200)
##
##winsound.Beep(233.08,200)
##
##winsound.Beep(246.94,200)
