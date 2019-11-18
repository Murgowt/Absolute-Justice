#Tkinter Imports
from tkinter import *
import tkinter.messagebox

def viewcomp():
    from . import complaint_view as cv
    cv.status()
def viewmiss():
    from . import missing_view as msv
    msv.view()
def callcitizen():
    from . import CITIZEN
    CITIZEN.view()

def viewcrimi():
    from . import crimi
    crimi.crimimenu()
def callpolice():
    from . import CITIZEN
    CITIZEN.view()
def gui():
    root = Tk()
    root.title('Absolute Justice')
    cmd = Label(root, text='Welcome!!Absolute Justice Prevails')
    cmd.pack(fill=X)

    topframe = Frame(root, height=200, width=600)
    midframe = Frame(root, height=200, width=600)
    botframe = Frame(root, height=200, width=600)

    topframe.pack(side=TOP)
    midframe.pack(side=TOP)
    botframe.pack(side=TOP)

    sq1 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Complaints', font=('Helvetica', '20'),command=viewcomp)
    sq1.pack(side=TOP)

    sq2 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Criminals', font=('Helvetica', '20'),command=viewcrimi)
    sq2.pack(side=TOP)

    sq3 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Missing Person', font=('Helvetica', '20'),command=viewmiss)
    sq3.pack(side=TOP)
    
    sq4 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Citizens', font=('Helvetica', '20'),command=callcitizen)
    sq4.pack(side=TOP)

    sq5 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Police', font=('Helvetica', '20'),command=callpolice)
    sq5.pack(side=TOP)

    sq6 = Button(topframe, height=2, width=100, bg="grey", fg="White", bd=4, text='Exit', font=('Helvetica', '20'),command=root.destroy)
    sq6.pack(side=TOP)
    root.mainloop()

if __name__ == '__main__':
    gui()
