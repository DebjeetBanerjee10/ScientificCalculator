import tkinter as tk 
from tkinter import *
import scipy.special as sp 
import numpy as np 
import distutils.core
import inspect
from enum import *


root = Tk()
root.geometry("300x300")
root.resizable(0,0)
canvas1 = Canvas(root,width = 300, height = 300)
canvas1.pack()

entry1 = Entry(root, width = 40)
canvas1.create_window(150,100, window = entry1)
label0 = Label(root, text = "calculator")
label0.config(font  =('helvetic, 20'))
canvas1.create_window(150, 40, window = label0)
def action(number):
    entry1.insert(END,number)

def clear():
    entry1.delete(0, END)




def result():
    res = str(entry1.get())
    try:
        output = eval(res)
        clear()
        entry1.insert(END, output)
    except:
        clear()
        entry1.insert(END, 'Invalid Input')
def percent():
    res = str(entry1.get())
    try:
        output2 = eval(res)
        result2 = output2*100
        clear()
        entry1.insert(END, result2)
    except:
        clear()
        entry1.insert(END, "Invalid Input")
def sin():
    val = str(entry1.get())
    try:
        val = int(val)
        res = sp.sindg(val)
        res = str(res)
        clear()
        entry1.insert(END, res)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def cos():
    val = str(entry1.get())
    try:
        val = int(val)
        res = sp.cosdg(val)
        res = str(res)
        clear()
        entry1.insert(END, res)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def tan():
    val = str(entry1.get())
    try:
        val = int(val)
        res = sp.tandg(val)
        res = str(res)
        clear()
        entry1.insert(END, res)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def cosec():
    val = str(entry1.get())
    try:
        val = int(val)
        res = sp.sindg(val)
        fres = 1/res
        clear()
        entry1.insert(END, fres)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def sec():
    val = str(entry1.get())
    try:
        val = int(val)
        res = sp.cosdg(val)
        fres = 1/res
        clear()
        entry1.insert(END, fres)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def cot():
    val = str(entry1.get())
    try:
        val = int(val)
        res = sp.tandg(val)
        fres = 1/res
        clear()
        entry1.insert(END, fres)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def square():
    val = str(entry1.get())
    try:
        val = int(val)
        res = val**2
        res = str(res)
        clear()
        entry1.insert(END, res)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def cube():
        val = str(entry1.get())
        try:
                val = int(val)
                res = val**3
                res = str(res)
                clear()
                entry1.insert(END, res)
        except:
                clear()
                entry1.insert(END, "Invalid Input")
def squareRoot():
    val = str(entry1.get())
    try:
        val = int(val)
        res = val**0.5
        res = str(res)
        clear()
        entry1.insert(END, res)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def ln():
    val = str(entry1.get())
    try:
        val = int(val)
        res = np.log(val)
        res = str(res)
        clear()
        entry1.insert(END, res)
    except:
        clear()
        entry1.insert(END, "Invalid Input")

def log():
        val = str(entry1.get())
        try:
                val = int(val)
                res = np.log10(val)
                res = str(res)
                clear()
                entry1.insert(END, res)
        except:
                clear()
                entry1.insert(END, "Invalid Input")

def e():

        res = 2.7182818285
        
        entry1.insert(END, res)
        
        
def fraction():
        val = str(entry1.get())
        res = "1/"+val
        clear()
        entry1.insert(END, res)

#extra functions:

butsin = Button(text = "sin", width = 5,bg = "powder blue", command = sin)
canvas1.create_window(23,150, window = butsin)
butcos = Button(text = "cos", width = 5,bg = "powder blue", command = cos)
canvas1.create_window(68,150, window = butcos)
buttan = Button(text = "tan", width = 5,bg = "powder blue", command = tan)
canvas1.create_window(113,150, window = buttan)
butcosec = Button(text = "cosec", width = 5,bg = "powder blue", command = cosec)
canvas1.create_window(23,175, window = butcosec)
butsec = Button(text = "sec", width = 5,bg = "powder blue", command = sec)
canvas1.create_window(68,175, window = butsec)
butcot = Button(text = "cot", width = 5,bg = "powder blue", command = cot)
canvas1.create_window(113,175, window = butcot)
butsq = Button(text = "x²", width = 5,bg = "powder blue", command = square)
canvas1.create_window(23,200, window = butsq)
butsqrt = Button(text = "√", width = 5,bg = "powder blue", command = squareRoot)
canvas1.create_window(68,200, window = butsqrt)
butcube = Button(text = "x3", width = 5,bg = "powder blue", command = cube)
canvas1.create_window(113,200, window = butcube)
butln = Button(text = "ln", width = 5,bg = "powder blue", command = ln)
canvas1.create_window(23,225, window = butln)
butlog = Button(text = "log", width = 5,bg = "powder blue", command = log)
canvas1.create_window(68,225, window = butlog)
bute = Button(text = "e", width = 5,bg = "powder blue", command = e)
canvas1.create_window(113,225, window = bute)
butfrc = Button(text = "1/x", width = 5,bg = "powder blue", command = fraction)
canvas1.create_window(23,250, window = butfrc)
butbr1 = Button(text = "(", width = 5,bg = "powder blue", command = lambda:action('('))
canvas1.create_window(68,250, window = butbr1)
butbr2 = Button(text = ")", width = 5,bg = "powder blue", command = lambda:action(')'))
canvas1.create_window(113,250, window = butbr2)
butAC = Button(text = "AC", width = 18 ,bg = "powder blue", command = clear)
canvas1.create_window(203, 150, window = butAC)
but1 = Button(text = "1", width = 5,  command = lambda:action('1'))
canvas1.create_window(158, 175, window = but1)
but2 = Button(text = "2", width = 5,  command = lambda:action('2'))
canvas1.create_window(203, 175, window = but2)
but3 = Button(text = "3", width = 5,  command = lambda:action('3'))
canvas1.create_window(248, 175, window = but3)
but4 = Button(text = "4", width = 5,  command = lambda:action('4'))
canvas1.create_window(158, 200, window = but4)
but5 = Button(text = "5", width = 5,  command = lambda:action('5'))
canvas1.create_window(203, 200, window = but5)
but6 = Button(text = "6", width = 5,  command = lambda:action('6'))
canvas1.create_window(248, 200, window = but6)
but7 = Button(text = "7", width = 5,  command = lambda:action('7'))
canvas1.create_window(158, 225, window = but7)
but8 = Button(text = "8", width = 5,  command = lambda:action('8'))
canvas1.create_window(203, 225, window = but8)
but9 = Button(text = "9", width = 5,  command = lambda:action('9'))
canvas1.create_window(248, 225, window = but9)
but0 = Button(text = "0", width = 5,  command = lambda:action('0'))
canvas1.create_window(158, 250, window = but0)
but00 = Button(text = "00", width = 5,  command = lambda:action('00'))
canvas1.create_window(203, 250, window = but00)
butp = Button(text = ".", width = 5,  command = lambda:action('.'))
canvas1.create_window(248, 250, window = butp)
butplus = Button(text = "+", width = 3, bg = "powder blue", command = lambda:action('+'))
canvas1.create_window(285, 150, window = butplus) 
butminus = Button(text = "-", width = 3, bg = "powder blue", command = lambda:action('-'))
canvas1.create_window(285, 175, window = butminus)
butmul = Button(text = "x", width = 3, bg = "powder blue", command = lambda:action('*'))
canvas1.create_window(285, 200, window = butmul)
butdiv = Button(text = "÷", width = 3, bg = "powder blue", command = lambda:action('/'))
canvas1.create_window(285, 225, window = butdiv)
butpercent = Button(text = "%", width = 3, bg = "powder blue", command = percent)
canvas1.create_window(285, 250, window = butpercent)
butequals = Button(text = "=", width = 43, height = 1, bg = "powder blue", command = result)
canvas1.create_window(150, 276, window = butequals)
root.mainloop()
