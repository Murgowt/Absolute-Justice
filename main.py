#Tkinter Imports
from tkinter import *
import tkinter.messagebox


def callPolice():
    from Police import basic
    basic.gui()
def callCitizen():
    from Citizen import Cpage
    Cpage.gui()
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

    sq1 = Button(topframe, height=6, width=100, bg="grey", fg="White", bd=4, text='Police', font=('Helvetica', '20'),command=callPolice)
    sq1.pack(side=TOP)

    sq2 = Button(topframe, height=6, width=100, bg="grey", fg="White", bd=4, text='Citizen', font=('Helvetica', '20'),command=callCitizen)
    sq2.pack(side=TOP)

    sq3 = Button(topframe, height=6, width=100, bg="grey", fg="White", bd=4, text='Exit', font=('Helvetica', '20'),command=exit)
    sq3.pack(side=TOP)

    root.mainloop()

if __name__ == '__main__':
    gui()
