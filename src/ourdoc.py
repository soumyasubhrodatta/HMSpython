from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install Pillow
rt=Tk()
rt.title("Our Doctors")
rt.geometry("1400x700+0+0")
bg2=ImageTk.PhotoImage(file="11.jpg")
frame=Label(rt,image=bg2)
frame.place(x=0,y=0,width=1360,height=800)
reg=Label(frame,text="Welcome to SSA Hospital",font=("Charlemagne Std",35,"bold"),fg="white",bg="dark blue")
reg.place(x=230,y=00,width=900)
reg1=Label(frame,text="OUR DOCTORS",font=("Charlemagne Std",25,"bold"),fg="white",bg="dark red")
reg1.place(x=420,y=80,width=500)
def gotomain():
    rt.destroy()
    import main
b3 = Button(frame, text="Go to Home", command=gotomain, font=("Times New Roman", 15, "bold"), fg="white",bg="dark blue")
b3.place(x=50, y=80)
def getdata(event):
    mycursor.execute("select * from doctor")
    currow = medtab.focus()
    contents = medtab.item(currow)
    row = contents['values']
    firstname.delete(0, END)
    lnm.delete(0, END)
    contact.delete(0, END)
    profession.delete(0, END)
    fees.delete(0, END)
    visit.delete(0, END)
    firstname.insert(0, row[0])
    lnm.insert(0, row[1])
    contact.insert(0, row[2])
    profession.insert(0, row[5])
    fees.insert(0, row[7])
    visit.insert(0, row[8])

def fectdata():
    db = mysql.connector.connect(host="localhost", user="root", password="Soumya123", database="hospital")
    mycursor = db.cursor()

    mycursor.execute("select firstname,lnm,contact,profession,fee,visit from doctor ")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        medtab.delete(*medtab.get_children())
    for row in rows:
        medtab.insert('', END, values=row)
    db.commit()
    db.close()

def fectdata1():
    ser1=comboser.get()
    lsearch1 = lsearch.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Soumya123", database="hospital")
    mycursor = db.cursor()

    mycursor.execute("select firstname,lnm,contact,profession,fee,visit from doctor where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        medtab.delete(*medtab.get_children())
    for row in rows:
       medtab.insert('',END,values=row)
    db.commit()
    db.close()
detfrm=Frame(rt,bd=4,relief=RIDGE,bg="dark blue")
detfrm.place(x=280,y=150,width=850,height=520)
lsearch=Label(detfrm,text="Search By",font=("Times New Roman",20,"bold"),bg="light blue")
lsearch.grid(row=0,column=0,pady=10,padx=20,sticky="w")
comboser=ttk.Combobox(detfrm,width=10,font=("Times New Roman",20,"bold"),state='readonly')
comboser['values']=("firstname","profession")
comboser.grid(row=0,column=1,padx=20,pady=10)
lsearch=Entry(detfrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")
serbt=Button(detfrm,text="Search",command=fectdata1,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
showbt=Button(detfrm,text="Show All",command=fectdata,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)
tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=20,y=70,width=800,height=400)
scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
medtab=ttk.Treeview(tabfrm,columns=("firstname","lnm","contact","profession","fees","visit"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("firstname",text="First Name")
medtab.heading("lnm",text="Last Name")
medtab.heading("contact",text="Contact No.")
medtab.heading("profession",text="Profession")
medtab.heading("fees",text="Fees")
medtab.heading("visit",text="Visit")
medtab['show']="headings"
medtab.column("firstname",width=100)
medtab.column("lnm",width=100)
medtab.column("contact",width=100)
medtab.column("profession",width=100)
medtab.column("fees",width=100)
medtab.column("visit",width=100)
medtab.pack(fill=BOTH,expand=1)
medtab.bind("<ButtonRelease-1>",getdata)
fectdata()
rt.mainloop()