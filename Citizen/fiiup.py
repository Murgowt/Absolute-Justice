import tkinter
from tkinter import ttk
import tkinter.messagebox
import os
import nib

import sys
sys.path.append("..")

def action(event,id_text,name_text,subj_text,doo_text,poo_text,des_text,dis_text,root):
    from . import DBMS_FinalC as DB
    id=id_text.get()
    name=name_text.get()
    subj=subj_text.get()
    doo=doo_text.get()
    poo=poo_text.get()
    des=des_text.get()
    dis=dis_text.get()
    cid=id+dis
    status='Investigating.'
    print(id, name, subj, doo, poo, des)
    DB.citizen_comp_register(name,id,cid,poo,doo,dis,subj,des,status)
    tkinter.messagebox.showinfo('Complaint Registered !!!','Complaint ID: '+cid)
    root.destroy()

def forms():

    root = tkinter.Tk()
    root.configure(background='grey')
    root.title("Complaints form")
    root.geometry("500x300")
    heading = ttk.Label(root, text="Form").grid(row=0, column=1)
    id_label= ttk.Label(root, text="Your ID").grid(row=1, column=0)
    name_label=ttk.Label(root,text="Name").grid(row=2, column=0)
    subj_label=ttk.Label(root,text="Subject").grid(row=3, column=0)
    doo_label=ttk.Label(root,text="Date").grid(row=4, column=0)
    poo_label=ttk.Label(root,text="Place").grid(row=5, column=0)
    des_label=ttk.Label(root,text="Description").grid(row=6, column=0)
    dis_label = ttk.Label(root, text="District").grid(row=7, column=0)
    id=tkinter.StringVar()
    name=tkinter.StringVar()
    subj=tkinter.StringVar()
    doo=tkinter.StringVar()
    poo=tkinter.StringVar()
    des=tkinter.StringVar()
    dis=tkinter.StringVar()
    id_text= ttk.Entry(root,textvariable=id)
    name_text = ttk.Entry(root,textvariable=name)
    subj_text= ttk.Entry(root,textvariable=subj)
    doo_text = ttk.Entry(root,textvariable=doo)
    poo_text = ttk.Entry(root,textvariable=poo)
    des_text = ttk.Entry(root,textvariable=des)
    dis_text = ttk.Entry(root, textvariable=dis)
    id_text.grid(row=1, column=1, ipadx="100")
    name_text.grid(row=2, column=1, ipadx="100")
    subj_text.grid(row=3, column=1, ipadx="100")
    doo_text.grid(row=4, column=1, ipadx="100")
    poo_text.grid(row=5, column=1, ipadx="100")
    des_text.grid(row=6, column=1, ipadx="100")
    dis_text.grid(row=7, column=1, ipadx="100")
    submit = tkinter.Button(root, text="Submit", fg="Black")
    submit.bind("<Button-1>", lambda event: action(event,id_text, name_text, subj_text, doo_text, poo_text, des_text,dis_text,root))
    submit.grid(row=9, column=1)

    id=id_text.get()
    name=name_text.get()
    subj=subj_text.get()
    doo=doo_text.get()
    poo=poo_text.get()
    des=des_text.get()
    print(id, name, subj, doo, poo, des)
    root.mainloop()