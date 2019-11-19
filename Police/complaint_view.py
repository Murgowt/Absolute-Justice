import tkinter
from tkinter import ttk
def action(event,dis_text,root):
    from . import DBMS_FinalP as DP
    dis = dis_text.get()
    rows=DP.police_signin_COMP(dis)
    strings = 'The Complaints in '+dis+"\n"
    print(rows)
    for row in rows:
        for i in row:
            strings = strings + i + "\n "
        strings = strings + '--------------------------------------\n'

    tkinter.messagebox.showinfo('Complaints', strings)
    root.destroy()
def status():
    root = tkinter.Tk()
    root.configure(background='grey')
    root.title("Status")
    root.geometry("300x50")
    status_label= ttk.Label(root, text="District").grid(row=0, column=0)
    dis = tkinter.StringVar()
    dis_text = ttk.Entry(root, textvariable=dis)
    dis_text.grid(row=0, column=1, ipadx="100")
    submit = tkinter.Button(root, text="Submit", fg="Black")
    submit.bind("<Button-1>",lambda event: action(event, dis_text,root))
    submit.grid(row=1, column=1)
    root.mainloop()