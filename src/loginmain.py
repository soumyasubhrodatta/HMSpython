from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
def login_window():
    rt.destroy()
    import login
def reg_win():
    rt.destroy()
    import register
def addmed():
    rt.destroy()
    import addmedicine
def doc_win():
    rt.destroy()
    import ourdoc
rt=Tk()
rt.title("Home Page")
rt.geometry("1400x700+0+0")


bg2=ImageTk.PhotoImage(file="bghome1.png")
frame=Label(rt,image=bg2)
frame.place(x=30,y=50,width=1300,height=630)

bg=ImageTk.PhotoImage(file="Hospital.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=70,y=230,width=600,height=300)

bg1=ImageTk.PhotoImage(file="Emergency.jpg")
logolb=Label(rt,image=bg1)
logolb.place(x=750,y=230,width=500,height=300)

logo1=ImageTk.PhotoImage(file="logo.jpg")
frame1=Label(rt,image=logo1)
frame1.place(x=160,y=65,width=90,height=90)

b4=Button(frame,text="Our doctors",command=doc_win,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b4.place(x=50,y=120)
reg=Label(frame,text="Welcome to SSA Hospital",font=("Charlemagne Std",35,"bold"),fg="white",bg="dark blue")
reg.place(x=230,y=30,width=900)
b1=Button(frame,text="Add Medicine",command=addmed,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b1.place(x=900,y=120)
b2=Button(frame,text="Login",command=login_window,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b2.place(x=1070,y=120)
b3=Button(frame,text="Register",command=reg_win,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b3.place(x=1170,y=120)

lb=Label(frame,text="Welcome to SSA Hospital. \n we have touched the lives of millions of patients of Kolkata, Eastern India and other neighbouring countries.\n Since its inception we are committed to provide highest standard of medical care which\n matches the global benchmark with extreme sensitivity to patient needs and privacy. ",font=("Georgia",15,"bold"),bg="black",fg="white")
lb.place(x=60,y=500,width=1200,height=120)
rt.mainloop()
