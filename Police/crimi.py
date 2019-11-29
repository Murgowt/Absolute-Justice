#Tkinter Imports
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
def crimiadd():
    from . import CRIMINALS_ADD as CD
    CD.missadd()
def crimiview():
    from . import CRIMINALS_VIEW as CV
    CV.view()
def crimimenu():
    root = Tk()
    root.title('Criminals')
    cmd = Label(root, text='Welcome!!Absolute Justice Prevails')
    cmd.pack(fill=X)
    topframe = Frame(root, height=200, width=200)
    topframe.pack(side=TOP)
    sq1 = Button(topframe, height=2, width=50, bg="grey", fg="White", bd=4, text='View Criminals',font=('Helvetica', '20'), command=crimiview)
    sq1.pack(side=TOP)
    sq2 = Button(topframe, height=2, width=50, bg="grey", fg="White", bd=4, text='Add Criminals',font=('Helvetica', '20'), command=crimiadd)
    sq2.pack(side=TOP)
    root.mainloop()