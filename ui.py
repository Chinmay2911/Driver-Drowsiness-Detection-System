# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:27:12 2019

@author: Lenovo
"""

from tkinter import *
from tkinter.ttk import *
import subprocess

def face():
    subprocess.call(["python", "face-try.py"])
    
def blink():
    subprocess.call(["python", "blinkDetect.py"])
    
def lane():
    subprocess.call(["python", "lanedetection.py"])
    
root = Tk() 
root.geometry('300x550') 
root.title('Drowsiness Detection System')

style = Style() 
style.configure('TButton', font =('calibri', 20, 'bold'), borderwidth = '2') 


# button 1 
btn1 = Button(root, text = 'Face Detection', command = face) 
btn1.grid(row =10, column = 0, padx = 30,pady=70) 

# button 2 
btn2 = Button(root, text = 'Blink Detection', command = blink) 
btn2.grid(row = 13, column = 0,  padx = 65) 

# button 2 
btn4 = Button(root, text = 'Lane Detection', command = lane) 
btn4.grid(row = 16, column = 0,  padx = 75,pady=70) 
#button 3
btn3 = Button(root, text = 'Quit', command = root.destroy) 
btn3.grid(row = 20, column = 0,  padx = 45)

    
root.mainloop() 
