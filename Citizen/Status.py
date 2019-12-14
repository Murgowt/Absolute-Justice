import tkinter
from tkinter import ttk
def action(event,id_text,root):
    from . import DBMS_FinalC as DB
    cid = id_text.get()
    status=DB.citizen_comp_status(cid)
    tkinter.messagebox.showinfo('Complaint Status!!!', 'Complaint Status: ' + status)
    root.destroy()
def status():
    root = tkinter.Tk()
    root.configure(background='grey')
    root.title("Status")
    root.geometry("300x50")
    status_label= ttk.Label(root, text="Complaint ID").grid(row=0, column=0)
    id = tkinter.StringVar()
    id_text = ttk.Entry(root, textvariable=id)
    id_text.grid(row=0, column=1, ipadx="100")
    submit = tkinter.Button(root, text="Submit", fg="Black")
    submit.bind("<Button-1>",lambda event: action(event, id_text,root))
    submit.grid(row=1, column=1)
    root.mainloop()
status()
