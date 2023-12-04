from tkinter import *
from tkinter import ttk 
import mysql.connector 
from tkinter import messagebox
from PIL import Image,ImageTk    

import random
import time
import datetime    

import hospital
import register
import forget_pwd
conn=mysql.connector.connect(host='localhost',user='root',password='1436')
cur=conn.cursor()
cur.execute('create database if not exists hospital')
cur.execute('use hospital')
cur.execute('create table if not exists register(fname varchar(50),lname varchar(50),contact char(10),email varchar(100),securityq varchar(50),securitya varchar(30),password varchar(20))')
cur.execute('create table if not exists record(patientid varchar(20),patientname varchar(45),patientissue varchar(100),patientcity varchar(45),patientfee varchar(45),patientgender char(6),patientdob date,patientage char(2),admitteddate date,fathername varchar(45),bloodgroup varchar(12),contactno char(10),aadharno char(14),nextvisit varchar(45),postcode varchar(12),bloodpressure varchar(45),roomno varchar(45),dischargedate date,referenceno varchar(45),email varchar(100),primary key(patientid,referenceno))')

conn.commit()

def login():
    if emst.get()=="" or pwdst.get()=="":
        messagebox.showerror("Error","All field are required")
            

            
    else:

        
        cur.execute("select * from register where email=%s and password=%s",(
            emst.get(),
            pwdst.get()
            ))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid Username & Password")
        else:
            open_main=messagebox.askyesno("Yes/No","Do you want to Continue")
            if open_main>0:
                
                hospital.Hospital()
                

                
                
                
                
                
            else:
                if not open_main:
                    return
        
        conn.commit()
        
        



def Login():
    def login():
        if emst.get()=="" or pwdst.get()=="":
            messagebox.showerror("Error","All field are required")
            

            
        else:

            cur.execute("select * from register where email=%s and password=%s",(
                emst.get(),
                pwdst.get()
                ))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Yes/No","Do you want to Continue")
                if open_main>0:
                    root.quit()
                    hospital.Hospital()
                    

                else:
                    if not open_main:
                        return
                

                
                
                
                
                
       
        
        conn.commit()
        conn.close()

    def regis():
        if evr.get()=="cher2reg":
            register.Register()
        else:
            messagebox.showerror('Error','Enetr the correct Password')
    
    

    def shpwd():
        if chbbtn.get()==0:
            pwd.config(show='*')
            e.config(show='*')
        else:
            pwd.config(show='')
            e.config(show='')
        
    global emst
    global pwdst
    root=Tk()
    root.title("Login")
    root.geometry("400x608+400+100") 
    root.resizable(0, 0)

    img2=Image.open("E:\Sample Pictures\loginicon.jpg")
    img2=img2.resize((130,130))
    bg=ImageTk.PhotoImage(img2)
    lblimg2=Label(image=bg,borderwidth=0)


    lblimg2.place(x=140,y=10)

    Label(root,text='Login Here',font=('Impact',38,'bold'),fg='red').place(x=90,y=120)


    img2=Image.open("E:\Sample Pictures\loginicon.jpg")
    img2=img2.resize((25,25))
    photoimage2=ImageTk.PhotoImage(img2)
    lblimg2=Label(image=photoimage2,bg='white',borderwidth=0)
    lblimg2.place(x=30,y=220,width=45,height=25)

    Label(root,text='E-Mail',font=('Times New Roman',13)).place(x=70,y=220)


    img3=Image.open("E:\Sample Pictures\images.jpg")
    img3=img3.resize((25,20))
    photoimage3=ImageTk.PhotoImage(img3)
    lblimg3=Label(image=photoimage3,bg='white',borderwidth=0)
    lblimg3.place(x=30,y=300,width=45,height=25)

    Label(root,text='Password',font=('Times New Roman',13)).place(x=70,y=300)

    emst=StringVar()
    pwdst=StringVar()
    chbbtn=IntVar()
    


    em=Entry(root,textvariable=emst,font=('times new roman',15),bg='light grey')
    em.place(x=50,y=250,width=300)

    pwd=Entry(root,textvariable=pwdst,show='*',font=('times new roman',15),bg='light grey')
    pwd.place(x=50,y=330,width=300)

    chb1=Checkbutton(root,text='Show password',variable=chbbtn,onvalue=1,offvalue=0,command=shpwd)
    chb1.place(x=50,y=380)
   


    b1=Button(root,text='Login',borderwidth=0,command=login,bg='red',fg='white',activeforeground='white',activebackground='red',font=('Times New Roman',15,'bold'))
    b1.place(x=130,y=420,height=40,width=140)

    Label(root,text="Enter the password to register",font=('times new roman',9)).place(x=40,y=520)
    
    global evr
    evr=StringVar()
    e=Entry(root,show='*',bg='Light grey',textvariable=evr)
    e.place(x=50,y=500)

    b2=Button(root,text='Register Here',command=regis,bg='white',activebackground='white')
    b2.place(x=220,y=500)

    b3=Button(root,text='Forget Password',command=forget_pwd.forget,bg='white',activebackground='white')
    b3.place(x=220,y=380)



    root.config(bg='white')
    root.mainloop()
    

Login()
