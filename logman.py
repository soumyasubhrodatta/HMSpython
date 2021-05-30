from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk
def main_win():
    rt.destroy()
    import managermain
def register_win():
    rt.destroy()
    import register
def log():
    rt.destroy()
    import login
def sel():
    if fmail.get() == "" or pwd1.get() == "":
        messagebox.showerror("Error All fields are required","Warning")
    else:
     nm=fmail.get()
     pwd2=pwd1.get()
     try:
        db=mysql.connector.connect(host="localhost",user="root",password="Soumya123",database="hospital")
        mycursor=db.cursor()
        mycursor.execute("select * from manager where email=%s and password=%s",(nm,pwd2))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid UserName and Password")
        else:
          messagebox.showinfo("Success", "Welcome")
          b3 = Button(frame, text="Go to Home", command=main_win, font=("Times New Roman", 15, "bold"), fg="white",
                      bg="dark blue")
          b3.place(x=200, y=260)
        db.commit()
     except EXCEPTION as e:
         print(e)
    db.rollback()
    db.close()
rt=Tk()
rt.title("Login")
rt.geometry("1400x800+0+0")

bg2=ImageTk.PhotoImage(file="22.jpg")
frame=Label(rt,image=bg2)
frame.place(x=30,y=30,width=1300,height=640)
reg=Label(frame,text="Welcome to SSA Hospital",font=("Charlemagne Std",35,"bold"),fg="white",bg="dark blue")
reg.place(x=230,y=30,width=900)

bg1=ImageTk.PhotoImage(file="4.jpg")
logolb=Label(rt,image=bg1)
logolb.place(x=120,y=195,width=640,height=390)

frame=Frame(rt,bg='white')
frame.place(x=580,y=190,width=600,height=400)
logg=Label(frame,text="Login",font=("Times New Roman",27,"bold"),fg="dark blue")
logg.place(x=80,y=20)
mailid=Label(frame,text="Enter Email Id",font=("Times New Roman",15,"bold"),bg="white")
mailid.place(x=30,y=100)
fmail=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
fmail.place(x=30,y=130,width=250)
pwd=Label(frame,text="Password",font=("Times New Roman",15,"bold"),bg="white")
pwd.place(x=30,y=190)
pwd1=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
pwd1.place(x=30,y=220,width=250)
pwd1.config(show="*")
b1=Button(frame,text="Login",command=sel,font=("Times New Roman",15,"bold"),fg="white",bg="dark blue")
b1.place(x=30,y=260)
reg=Button(frame,command=register_win,cursor="hand2",text="Register New Account",font=("Times New Roman",15,"bold"),bg="dark blue",fg="white")
reg.place(x=30,y=320)

reg1=Button(frame,command=log,cursor="hand2",text="Go back to Login Portal",font=("Times New Roman",15,"bold"),bg="dark blue",fg="white")
reg1.place(x=270,y=320)

rt.mainloop()
