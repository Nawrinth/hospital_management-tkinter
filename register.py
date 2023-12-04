from tkinter import *
from tkinter import ttk,messagebox   
import mysql.connector as sql 

def Register():
    def reg():
        c=0
        for i in conno.get():
            if i.isdigit():
                continue
            else:
                c=c+1
        if fname.get()=='' or lname.get()=='' or conno.get()=='' or emailstr.get()=='' or seca.get()=='' or pwd.get()=='' or cpwd.get()=='':
            messagebox.showerror("Error",'All fields are required')
        elif c!=0:
            messagebox.showerror('Error','Enter the correct Contact Number')
        
        elif secq.get()=='Select':
            messagebox.showerror('Error','Select a proper question')
        elif pwd.get()!=cpwd.get():
            messagebox.showerror("Error",'Enter the correct password ')
        else:
            con=sql.connect(host='localhost',user='root',password='1436',database='hospital')
            cursor=con.cursor()
            cursor.execute("SELECT * FROM REGISTER WHERE EMAIL=%s",(emailstr.get(),))
            row=cursor.fetchone()
            if row==None:

                query='INSERT INTO REGISTER VALUES (%s,%s,%s,%s,%s,%s,%s)'
                values=(fname.get(),lname.get(),conno.get(),emailstr.get(),secq.get(),seca.get(),pwd.get())
                cursor.execute(query,values)
                messagebox.showinfo("Info","Record inserted Successfully")
                con.commit()
                root.destroy()
            else:
                messagebox.showerror("Error","Email already exist")
        
    root=Toplevel()
    root.geometry('800x600+100+20')
    root.config(bg='Light grey')

    Label(root,text='REGISTER HERE',bg='Light Grey',font=('times new rooman',35,'bold'),fg='GREEN').place(x=230,y=10)
    #Gobal variable
    global fname
    global lname
    global conno
    global emailstr
    global secq
    global seca
    global pwd
    global cpwd

    #Variable declaration
    fname=StringVar()
    lname=StringVar()
    conno=StringVar()
    emailstr=StringVar()
    secq=StringVar()
    seca=StringVar()
    pwd=StringVar()
    cpwd=StringVar()


    #first Name
    Label(root,text='First Name',font=('Times new roman',15),bg='Light Grey').place(x=10,y=110)

    efname=Entry(root,textvariable=fname,width=32)
    efname.place(x=130,y=113)
    
    #Last name
    Label(root,text='Last Name',font=('Times new roman',15),bg='Light Grey').place(x=10,y=190)

    lfname=Entry(root,textvariable=lname,width=32)
    lfname.place(x=130,y=193)

    #Contact Number
    Label(root,text='Contact No',font=('Times new roman',15),bg='Light Grey').place(x=10,y=270)

    ecno=Entry(root,textvariable=conno,width=32)
    ecno.place(x=130,y=273)

    #Email Id
    Label(root,text='Email',font=('Times new roman',15),bg='Light Grey').place(x=10,y=350)

    eemail=Entry(root,textvariable=emailstr,width=32)
    eemail.place(x=130,y=353)

    #Securith Question
    Label(root,text='Security Question',font=('Times new roman',15),bg='Light Grey').place(x=380,y=110)

    combo_secques=ttk.Combobox(root,font=("times new roman",12),state="readonly",textvariable=secq)
    combo_secques['values']=("Select","Your Birth Place","Your Pet Name","Favourite Actor")
    combo_secques.place(x=550,y=110,width=200)
    combo_secques.current(0)

    #Security Answer
    Label(root,text='Security Answer',font=('Times new roman',15),bg='Light Grey').place(x=380,y=190)

    sa=Entry(root,textvariable=seca,width=32)
    sa.place(x=550,y=190)

    #Password
    Label(root,text='Password',font=('Times new roman',15),bg='Light Grey').place(x=380,y=270)

    p=Entry(root,textvariable=pwd,width=32)
    p.place(x=550,y=270)

    #Confirm Password
    Label(root,text='Confirm Password',font=('Times new roman',15),bg='Light Grey').place(x=380,y=350)

    cp=Entry(root,textvariable=cpwd,width=32)
    cp.place(x=550,y=350)

    #Button
    btn=Button(root,text='Register Here',bg='green',activebackground='green',font=('times new roman',23),command=reg)
    btn.place(x=330,y=450)
    
    root.mainloop()


