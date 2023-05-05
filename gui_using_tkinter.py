from tkinter import *
from PIL import Image
root=Tk()
root.title("Create an account")
root.geometry("1200x700")
descr=Label(root,text="Create an account now!")
descr.pack()
entry=Entry(root)




obj=Button(root,text="Password",bd=5)
obj.pack()
entry.pack()

root.mainloop()