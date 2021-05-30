from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk #pip install Pillow
def main_window():
    rt.destroy()
    import managermain

def Add():
    if p1.get()=="" or fen.get()=="" or len.get()=="" or cont.get()=="" or add.get()=="":
        messagebox.showerror("Error","All fields are required")

    elif vag.get()==0:
        messagebox.showerror("Error", "please agree our term and codition")
    else:
     pid=p1.get()
     nm=fen.get()
     lm=len.get()
     cont1=cont.get()
     dob1=cal.get()

     gen1=radio.get()
     address1=add.get()
     blg1=bldgrp.get()
     disease1=d.get()
     symptoms1=s.get()
     pd1=p.get()
     db=mysql.connector.connect(host="localhost",user="root",password="Soumya123",database="hospital")
     mycursor=db.cursor()
     print("connected")
     try:
        sql="insert into admission(patid,firstname,lnm,contact,dob,gen,address,blg,disease,symptoms,pd)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(pid,nm,lm,cont1,dob1,gen1,address1,blg1,disease1,symptoms1,pd1)
        mycursor.execute(sql,val)
        db.commit()
        lastid=mycursor.lastrowid
        messagebox.showinfo("information","Record Inserted successfully")
        pid.delete(0, END)
        nm.delete(0,END)
        lm.delete(0, END)
        cont1.delete(0, END)
        dob1.delete(0, END)

        gen1.delete(0, END)
        address1.delete(0, END)
        blg1.delete(0, END)
        disease1.delete(0, END)
        symptoms1.delete(0, END)
        pd1.delete(0, END)

        pid.focus_set()
     except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()

rt=Tk()
rt.title("Register")
rt.geometry("1400x700+0+0")

bg2=ImageTk.PhotoImage(file="logbg.jpg")
frame=Label(rt,image=bg2)
frame.place(x=30,y=20,width=1300,height=730)
reg=Label(frame,text="Welcome to SSA Hospital",font=("Charlemagne Std",35,"bold"),fg="white",bg="dark blue")
reg.place(x=230,y=25,width=900)
bg1=ImageTk.PhotoImage(file="loginbg.jpg")
logolb=Label(rt,image=bg1)
logolb.place(x=50,y=200,width=800,height=400)
frame=Frame(rt,bg='white')
frame.place(x=520,y=130,width=800,height=540)
reg=Label(frame,text="ADMISSION AND APPOINTMENTS",font=("Times New Roman",25,"bold"),fg="dark blue",bg="White")
reg.place(x=20,y=20)
p2=Label(frame,text="PATIENT ID",font=("Times New Roman",15,"bold"),bg="white")
p2.place(x=650,y=80)
p1=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
p1.place(x=650,y=110,width=100)
fnm=Label(frame,text="First Name",font=("Times New Roman",15,"bold"),bg="white")
fnm.place(x=30,y=80)
fen=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
fen.place(x=30,y=110,width=250)
lnm=Label(frame,text="Last Name",font=("Times New Roman",15,"bold"),bg="white")
lnm.place(x=370,y=80)
len=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
len.place(x=370,y=110,width=250)
contact=Label(frame,text="Contact Number",font=("Times New Roman",15,"bold"),bg="white")
contact.place(x=30,y=140)
cont=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
cont.place(x=30,y=170,width=250)
dob=Label(frame,text="DOB",font=("Times New Roman",15,"bold"),bg="white")
dob.place(x=370,y=140)
cal = DateEntry(frame,font=("Times New Roman",15,"bold"),background='gray',foreground='white',borderwidth=2)
cal.place(x=370,y=170,width=250,height=30)

gen=Label(frame,text="Gender",font=("Times New Roman",15,"bold"),bg="white")
gen.place(x=370,y=220)
radio = StringVar()
m = Radiobutton(frame,text="Male",variable=radio,value="Male",bg="white",font=("Times New Roman",15,"bold"))
m.place(x=370,y=250,width=130,height=20)
f=Radiobutton(frame, text="Female", variable=radio, value="Female",bg="White",font=("Times New Roman",15,"bold"))
f.place(x=370,y=270,width=150,height=20)


ad=Label(frame,text="Address",font=("Times New Roman",15,"bold"),bg="white")
ad.place(x=30,y=200)
add=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
add.place(x=30,y=230,width=300)


blood=Label(frame,text="Blood Group",font=("Times New Roman",15,"bold"),bg="white")
blood.place(x=30,y=260)
bldgrp=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
bldgrp.place(x=30,y=290,width=250)

d1=Label(frame,text="Disease",font=("Times New Roman",15,"bold"),bg="white")
d1.place(x=30,y=320)
d=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
d.place(x=30,y=350,width=250)

s1=Label(frame,text="Symptoms",font=("Times New Roman",15,"bold"),bg="white")
s1.place(x=370,y=320)
s=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
s.place(x=370,y=350,width=250)

pd1=Label(frame,text="Prefered Doctor",font=("Times New Roman",15,"bold"),bg="white")
pd1.place(x=370,y=390)
p=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
p.place(x=370,y=420,width=250)




vag=IntVar()
chk=Checkbutton(frame,variable=vag,text="I Agree the Terms and Conditions",font=("Times New Roman",10,"bold"),onvalue=1,offvalue=0)
chk.place(x=370,y=480)
b1=Button(frame,text="Submit",command=Add,font=("Times New Roman",15,"bold"),bg="dark blue",fg="white")
b1.place(x=30,y=410)
b5=Button(frame,text="Return to main",command=main_window,font=("Times New Roman",15,"bold"),fg="white",bg="blue")
b5.place(x=30,y=470)

rt.mainloop()
