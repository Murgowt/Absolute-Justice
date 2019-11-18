#Tkinter Imports
from tkinter import *
import tkinter.messagebox


#Basic Intiations
def callFR():
    print(123)
    from . import Recognizer
    Recognizer.recognizers()

def calltrainer():
    print(1321)
    from . import SignUp as SU
    SU.forms()

def gui():
    root = Tk()
    root.title('Police')
    cmd = Label(root, text='Welcome!!Absolute Justice Prevails')
    cmd.pack(fill=X)
    topframe=Frame(root,height=200,width=600)
    topframe.pack(side=TOP)

    sq1=Button(topframe,height=6,width=100,bg="grey",fg="White",bd=4,text='Log-In',font=('Helvetica', '20'),command=callFR)
    sq1.pack(side=TOP)

    sq2=Button(topframe,height=6,width=100,bg="grey",fg="White",bd=4,text='Sign-Up',font=('Helvetica', '20'),command=calltrainer)
    sq2.pack(side=TOP)

    sq3=Button(topframe,height=6,width=100,bg="grey",fg="White",bd=4,text='Exit',font=('Helvetica', '20'),command=root.destroy)
    sq3.pack(side=TOP)

    root.mainloop()

