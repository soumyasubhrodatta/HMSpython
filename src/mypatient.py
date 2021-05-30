from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install Pillow

def gotomain():
    rt.destroy()
    import docmain

rt=Tk()
rt.title("My Patients")
rt.geometry("1400x700+0+0")

bg2=ImageTk.PhotoImage(file="9.jpg")
frame=Label(rt,image=bg2)
frame.place(x=0,y=0,width=1500,height=1200)

reg=Label(frame,text="Welcome to SSA Hospital",font=("Charlemagne Std",35,"bold"),fg="white",bg="dark blue")
reg.place(x=230,y=00,width=900)
reg1=Label(frame,text="MY PATIENTS",font=("Charlemagne Std",25,"bold"),fg="white",bg="dark red")
reg1.place(x=420,y=80,width=500)

mangefrm=Frame(rt,bd=4,relief=RIDGE,bg="dark blue")
mangefrm.place(x=20,y=150,width=450,height=540)
mtitle=Label(mangefrm,text="Patient Details",font=("Times New Roman",20,"bold"),fg="darkgreen",bg="light blue")
mtitle.grid(row=0,columnspan=2,pady=20)
icd=Label(mangefrm,text="Patient ID",font=("Times New Roman",15,"bold"),bg="light blue")
icd.grid(row=1,column=0,pady=10,padx=20,sticky="w")
icd1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
icd1.grid(row=1,column=1,pady=10,padx=20,sticky="w")

inm=Label(mangefrm,text="First Name",font=("Times New Roman",15,"bold"),bg="light blue")
inm.grid(row=2,column=0,pady=10,padx=20,sticky="w")
fnm1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
fnm1.grid(row=2,column=1,pady=10,padx=20,sticky="w")
unitp=Label(mangefrm,text="Last Name",font=("Times New Roman",15,"bold"),bg="light blue")
unitp.grid(row=3,column=0,pady=10,padx=20,sticky="w")
lnm1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
lnm1.grid(row=3,column=1,pady=10,padx=20,sticky="w")
qty=Label(mangefrm,text="Blood Group",font=("Times New Roman",15,"bold"),bg="light blue")
qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")
blg2=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
blg2.grid(row=4,column=1,pady=10,padx=20,sticky="w")
unit1=Label(mangefrm,text="Disease",font=("Times New Roman",15,"bold"),bg="light blue")
unit1.grid(row=5,column=0,pady=10,padx=20,sticky="w")
dis1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
dis1.grid(row=5,column=1,pady=10,padx=20,sticky="w")
unit2=Label(mangefrm,text="Symptoms",font=("Times New Roman",15,"bold"),bg="light blue")
unit2.grid(row=6,column=0,pady=10,padx=20,sticky="w")

sysm1=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
sysm1.grid(row=6,column=1,pady=10,padx=20,sticky="w")
unit3=Label(mangefrm,text="Doctor",font=("Times New Roman",15,"bold"),bg="light blue")
unit3.grid(row=7,column=0,pady=10,padx=20,sticky="w")

pd2=Entry(mangefrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
pd2.grid(row=7,column=1,pady=10,padx=20,sticky="w")

btnfrm=Frame(mangefrm,bd=4,relief=RIDGE,bg="black")
btnfrm.place(x=70,y=460,width=210,height=60)


def update():
    pid = icd1.get()
    dis = dis1.get()
    sysm = sysm1.get()


    db = mysql.connector.connect(host="localhost", user="root", password="Soumya123", database="hospital")
    mycursor = db.cursor()

    try:
        sql = "update admission set disease=%s,symptoms=%s where patid=%s"
        val = (dis, sysm, pid)
        mycursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("information", "Record Updated successfully")
        icd1.delete(0, END)

        dis1.delete(0, END)
        sysm1.delete(0, END)
        print("done")
        fectdata()
        print("done")
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()

def fectdata():
    pid = icd1.get()
    fnm = fnm1.get()
    lnm = lnm1.get()

    blg1 = blg2.get()
    dis = dis1.get()
    sysm = sysm1.get()
    pd1 = pd2.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Soumya123", database="hospital")
    mycursor = db.cursor()
    sql=mycursor.execute("select patid,firstname,lnm,blg,disease,symptoms,pd from admission")
    val = (pid, fnm, lnm, blg1, dis, sysm, pd1)
    mycursor.execute(sql, val)
    rows=mycursor.fetchall()
    if len(rows)!=0:
        medtab.delete(*medtab.get_children())
    for row in rows:
       medtab.insert('',END,values=row)
    db.commit()
    db.close()

def cleardata():
    icd1.delete(0, 'end')
    fnm1.delete(0, 'end')
    lnm1.delete(0, 'end')
    blg2.delete(0, 'end')
    dis1.delete(0 , 'end')
    sysm1.delete(0, 'end')
    pd2.focus_set()
    icd1.focus_set()
def getdata(event):
    currow=medtab.focus()
    contents=medtab.item(currow)
    row=contents['values']
    icd1.delete(0, END)
    fnm1.delete(0, END)
    lnm1.delete(0, END)
    blg2.delete(0, END)
    dis1.delete(0, END)
    sysm1.delete(0, END)
    pd2.delete(0, END)
    icd1.insert(0,row[0])
    fnm1.insert(0,row[1])
    lnm1.insert(0,row[2])
    blg2.insert(0,row[3])
    dis1.insert(0,row[4])
    sysm1.insert(0, row[5])
    pd2.insert(0, row[6])

'''def delete1():
    firstname = icd1.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Soumya123", database="hospital")
    mycursor = db.cursor()
    try:
        sql = "delete from admission where itemcode=%s"
        val = (firstname,)
        mycursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("information", "Record Deleted successfully")
        icd1.delete(0, END)
        inm1.delete(0, END)
        unitp1.delete(0, END)
        qty1.delete(0, END)
        unit2.delete(0, END)
        fectdata()
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()'''
def fectdata1():
    ser1=comboser.get()
    lsearch1 = lsearch.get()
    db = mysql.connector.connect(host="localhost", user="root", password="Soumya123", database="hospital")
    mycursor = db.cursor()
    mycursor.execute("select patid,firstname,lnm,blg,disease,symptoms,pd from admission where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        medtab.delete(*medtab.get_children())
    for row in rows:
       medtab.insert('',END,values=row)
    db.commit()
    db.close()


updatebt=Button(btnfrm,text="UPDATE",command=update,width=10).grid(row=0,column=1,padx=10,pady=10)

clrt=Button(btnfrm,text="CLEAR",command=cleardata,width=10).grid(row=0,column=3,padx=10,pady=10)

b2=Button(frame,text="Home",command=gotomain,font=("Times New Roman",15,"bold"),fg="white",bg="blue").grid(row=1,column=3,padx=10,pady=10)

detfrm=Frame(rt,bd=4,relief=RIDGE,bg="dark blue")
detfrm.place(x=500,y=170,width=850,height=450)
lsearch=Label(detfrm,text="Search By",font=("Times New Roman",20,"bold"),bg="light blue")
lsearch.grid(row=0,column=0,pady=10,padx=20,sticky="w")
comboser=ttk.Combobox(detfrm,width=10,font=("Times New Roman",20,"bold"),state='readonly')
comboser['values']=("pd","patid")
comboser.grid(row=0,column=1,padx=20,pady=10)
lsearch=Entry(detfrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")
serbt=Button(detfrm,text="Search",command=fectdata1,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
showbt=Button(detfrm,text="Show All",command=fectdata,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)
tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=70,width=800,height=350)
scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
medtab=ttk.Treeview(tabfrm,columns=("pid","firstname","lnm","blg","disease","symptoms","pd1"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("pid",text="Patient Code")
medtab.heading("firstname",text="First Name")
medtab.heading("lnm",text="Last Name")
medtab.heading("blg",text="Blood group")
medtab.heading("disease",text="Disease")
medtab.heading("symptoms",text="Symptoms")
medtab.heading("pd1",text="Doctor")
medtab['show']="headings"
medtab.column("pid",width=100)
medtab.column("firstname",width=100)
medtab.column("lnm",width=100)
medtab.column("blg",width=100)
medtab.column("disease",width=100)
medtab.column("symptoms",width=100)
medtab.column("pd1",width=100)

medtab.pack(fill=BOTH,expand=1)
medtab.bind("<ButtonRelease-1>",getdata)
fectdata()
rt.mainloop()
