import tkinter
from tkinter import ttk
def action(event,id_text,root):
    from . import DBMS_FinalP as DP
    dis = id_text.get()
    rows=DP.police_signin_citizen(dis)
    strings =''
    print(rows)
    for row in rows:
        for i in row:
            strings = strings + str(i) + "\n "
        strings = strings + '--------------------------------------\n'

    tkinter.messagebox.showinfo('Missing People', strings)
    root.destroy()
def view():
    root = tkinter.Tk()
    root.configure(background='grey')
    root.title("Citizen")
    root.geometry("300x50")
    missing_label= ttk.Label(root, text="District").grid(row=0, column=0)
    dis = tkinter.StringVar()
    dis_text = ttk.Entry(root, textvariable=id)
    dis_text.grid(row=0, column=1, ipadx="100")
    submit = tkinter.Button(root, text="Submit", fg="Black")
    submit.bind("<Button-1>",lambda event: action(event, dis_text,root))
    submit.grid(row=1, column=1)
    root.mainloop()
view()
