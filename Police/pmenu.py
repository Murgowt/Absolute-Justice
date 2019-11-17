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
