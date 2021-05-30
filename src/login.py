from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
def main_win():
    rt.destroy()
    import loginmain
def register_win():
    rt.destroy()
    import register
def logdoc_win():
    rt.destroy()
    import logdoc
def logman_win():
    rt.destroy()
    import logman
def lognurse_win():
    rt.destroy()
    import lognurse


rt=Tk()
rt.title("Login")
rt.geometry("1400x800+0+0")

bg2=ImageTk.PhotoImage(file="large.jpg")
frame=Label(rt,image=bg2)
frame.place(x=30,y=30,width=1300,height=630)
reg=Label(frame,text="Welcome to SSA Hospital",font=("Charlemagne Std",35,"bold"),fg="white",bg="dark blue")
reg.place(x=230,y=30,width=900)

bg1=ImageTk.PhotoImage(file="small.jpg")
logolb=Label(rt,image=bg1)
logolb.place(x=120,y=220,width=470,height=330)

frame=Frame(rt,bg='white')
frame.place(x=580,y=190,width=600,height=400)

bg3=ImageTk.PhotoImage(file="logincom.jpeg")
logolb1=Label(rt,image=bg3)
logolb1.place(x=850,y=260,width=280,height=230)


logg=Label(frame,text="Login",font=("Times New Roman",27,"bold"),fg="dark blue")
logg.place(x=80,y=20)
reg=Button(frame,command=logdoc_win,cursor="hand2",text="Doctor's Portal",font=("Times New Roman",15,"bold"),bg="dark blue",fg="white")
reg.place(x=30,y=100)
reg=Button(frame,command=lognurse_win,cursor="hand2",text="Nurse's Portal",font=("Times New Roman",15,"bold"),bg="dark blue",fg="white")
reg.place(x=30,y=150)
reg=Button(frame,command=logman_win,cursor="hand2",text="Manager's Portal",font=("Times New Roman",15,"bold"),bg="dark blue",fg="white")
reg.place(x=30,y=200)

reg=Button(frame,command=register_win,cursor="hand2",text="Register New Account",font=("Times New Roman",15,"bold"),bg="dark blue",fg="white")
reg.place(x=30,y=320)

rt.mainloop()
