#Tkinter Imports
from tkinter import *
import tkinter.messagebox

def callfiip():
    from . import fiiup
    fiiup.forms()

def callstatus():
    from . import Status
    Status.status()

def callmiss():
    from . import missing
    missing.missmenu()

def callpolice():
    from . import POLICEC
    POLICEC.view()

def viewcrimi():
    from . import Criminals
    Criminals.view()
def gui():
    root = Tk()
    root.title('Citizen')
    cmd = Label(root, text='Welcome!!Absolute Justice Prevails')
    cmd.pack(fill=X)
    topframe=Frame(root,height=200,width=600)
    topframe.pack(side=TOP)

    sq1=Button(topframe,height=2,width=100,bg="grey",fg="White",bd=4,text='Complaint Register',font=('Helvetica', '20'),command=callfiip)
    sq1.pack(side=TOP)

    sq2=Button(topframe,height=2,width=100,bg="grey",fg="White",bd=4,text='Complaint Status',font=('Helvetica', '20'),command=callstatus)
    sq2.pack(side=TOP)

    sq3=Button(topframe,height=2,width=100,bg="grey",fg="White",bd=4,text='Missing Person',font=('Helvetica', '20'),command=callmiss)
    sq3.pack(side=TOP)

    sq4 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Criminals', font=('Helvetica', '20'),command=viewcrimi)
    sq4.pack(side=TOP)

    sq5 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Police', font=('Helvetica', '20'),command=callpolice)
    sq5.pack(side=TOP)

    sq6 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Exit', font=('Helvetica', '20'),command=root.destroy)
    sq6.pack(side=TOP)

    root.mainloop()

gui()