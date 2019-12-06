#Tkinter Imports
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
def missadd():
    from . import missing_add as ma
    ma.missadd()
def missview():
    from . import missing_view as msv
    msv.view()
def missmenu():
    root = Tk()
    root.title('Missing Persons')
    cmd = Label(root, text='Welcome!!Absolute Justice Prevails')
    cmd.pack(fill=X)
    topframe = Frame(root, height=200, width=200)
    topframe.pack(side=TOP)
    sq1 = Button(topframe, height=2, width=50, bg="grey", fg="White", bd=4, text='View Missing Persons',font=('Helvetica', '20'), command=missview)
    sq1.pack(side=TOP)
    sq2 = Button(topframe, height=2, width=50, bg="grey", fg="White", bd=4, text='Add Missing Persons',font=('Helvetica', '20'), command=missadd)
    sq2.pack(side=TOP)
    root.mainloop()