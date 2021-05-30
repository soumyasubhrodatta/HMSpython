from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk #pip install Pillow
def login_window():
    rt.destroy()
    import login

def doc_window():
    rt.destroy()
    import doc

def employ_window():
    rt.destroy()
    import register1

def nurse_window():
    rt.destroy()
    import nurse

def man_window():
    rt.destroy()
    import manager

rt=Tk()
rt.title("Register")
rt.geometry("1400x700+0+0")

bg2=ImageTk.PhotoImage(file="rbg.jpg")
frame=Label(rt,image=bg2)
frame.place(x=30,y=20,width=1300,height=670)
reg=Label(frame,text="Welcome to SSA Hospital",font=("Charlemagne Std",35,"bold"),fg="white",bg="dark blue")
reg.place(x=230,y=25,width=900)
bg1=ImageTk.PhotoImage(file="loginbg.jpg")
logolb=Label(rt,image=bg1)
logolb.place(x=50,y=200,width=800,height=400)
bg3=ImageTk.PhotoImage(file="nurses.jpg")
loglb=Label(rt,image=bg3)
loglb.place(x=900,y=200,width=400,height=400)
frame=Frame(rt,bg='white')
frame.place(x=500,y=150,width=400,height=500)
reg=Label(frame,text="REGISTER HERE",font=("Times New Roman",25,"bold"),fg="dark blue",bg="White")
reg.place(x=20,y=20)

frame=Frame(rt,bg='sky blue')
frame.place(x=530,y=240,width=300,height=350)

b2=Button(frame,text="DOCTOR",command=doc_window,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b2.place(x=80,y=50)
b3=Button(frame,text="NURSE",command=nurse_window,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b3.place(x=80,y=120)
b4=Button(frame,text="MANAGER",command=man_window,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b4.place(x=80,y=190)
b5=Button(frame,text="EMPLOYEE",command=employ_window,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b5.place(x=80,y=260)



rt.mainloop()
