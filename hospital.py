from tkinter import *
from tkinter import ttk 
from tkinter import messagebox  

import random
import time
import datetime    
import mysql.connector 


def Hospital():
    
    def get_time():
        timevar = time.strftime("%I:%M:%S %p")
        clock.config(text=timevar)
        clock.after(200,get_time)
        
    def srch():
        
        if srchop.get()=="":
            messagebox.showerror("Error","Enter the paitent detail to Search")
        else:
            
            conn=mysql.connector.connect(host='localhost',user='root',password='1436',database='hospital')
            mycr=conn.cursor()
            
            if selectinp.get()=="PAITENTID":
            
                mycr.execute("SELECT * FROM RECORD WHERE PAITENTID LIKE %s",(srchop.get(),))
                data=mycr.fetchall()
                print(data)
            
                if len(data)!=0:
                    lbox.delete(*lbox.get_children())
                    for i in data:
                        lbox.insert("",END,values=i)
            
                else:
                    lbox.delete(*lbox.get_children())
                
            elif selectinp.get()=="CONTACTNO":
                mycr.execute("SELECT * FROM RECORD WHERE CONTACTNO LIKE %s",(srchop.get(),))
                data=mycr.fetchall()
                print(data)
            
                if len(data)!=0:
                    lbox.delete(*lbox.get_children())
                    for i in data:
                        lbox.insert("",END,values=i)
                
                else:
                    lbox.delete(*lbox.get_children())
                
            elif selectinp.get()=="REFERENCENO":
                mycr.execute("SELECT * FROM RECORD WHERE REFERENCENO LIKE %s",(srchop.get(),))
                data=mycr.fetchall()
                print(data)
               
                if len(data)!=0:
                    lbox.delete(*lbox.get_children())
                    for i in data:
                        lbox.insert("",END,values=i)
                else:
                    lbox.delete(*lbox.get_children())
                    
            conn.close()
            
            
            
        
    def paid():
        
        Pay = random.randint(20000, 709467)
        Paid = ("PID" + str(Pay))
        paitentid.set(Paid)
        
        
        refno = random.randint(20000, 709467)
        Ref = ("RNO" + str(refno))
        referenceno.set(Ref)
        
        

        
        
    def exits():
        open_main=messagebox.askyesno("Info","Do you want to exit")
        if open_main>0:
            root.destroy()
        
        
    def deleterec():
        if paitentid.get()=="":
            messagebox.showerror("Error",'Enter the Paitent Id')
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='1436',database='hospital')
            mycr=conn.cursor()
        
            mycr.execute("SELECT * FROM RECORD WHERE PAITENTID=%s",(paitentid.get(),))
            row=mycr.fetchone()
            if row!=None:
        
                mycr.execute("DELETE FROM RECORD WHERE paitentid=%s",(paitentid.get(),))
                messagebox.showinfo("Info","Record deleted Successfuly")
        
            else:
                messagebox.showerror("Error","enter the proppaitentid")
            
            conn.commit()
            conn.close()
            
            
            
        
    def pescdata():
        if paitentid.get()=="" or referenceno.get()=="" or paitentname.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        elif paitentgender.get()=="Select":
            messagebox.showerror("Error","Select The Gender Properly")
            
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='1436',database='hospital')
            mycr=conn.cursor()
            
            mycr.execute("insert into record values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                 (paitentid.get(),
                 paitentname.get(),
                 paitentissue.get(),
                 paitentcity.get(),
                 paitentfee.get(),
                 paitentgender.get(),
                 paitentdob.get(),
                 paitentage.get(),
                 admitteddate.get(),
                 fathername.get(),
                 bloodgroup.get(),
                 contactno.get(),
                 aadharno.get(),
                 nextvisit.get(),
                 postcode.get(),
                 bloodpressure.get(),
                 roomno.get(),
                 dischargedate.get(),
                 referenceno.get(),
                 email.get()))
            
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Info","Values inserted Successfuly")
            epid.delete(0,END)
            epname.delete(0,END)
            epissue.delete(0,END)
            epcity.delete(0,END)
            epfee.delete(0,END)
            comgen.current(0)
            epdob.delete(0,END)
            epage.delete(0,END)
            epdoa.delete(0,END)
            eFHname.delete(0,END)
            ebgro.delete(0,END)
            epcno.delete(0,END)
            eaano.delete(0,END)
            envis.delete(0,END)
            epost.delete(0,END)
            ebpre.delete(0,END)
            eroomno.delete(0,END)
            edod.delete(0,END)
            erefno.delete(0,END)
            eemail.delete(0,END)
            
    def  update():
        
        
        if paitentid.get()=="":
            messagebox.showerror("Error",'Enter the Paitent Id')
        else:
            mysqldb=mysql.connector.connect(host='localhost',port='3306',user='root',password="1436",database='hospital')
            mycursor=mysqldb.cursor()
            mycursor.execute("SELECT * FROM RECORD WHERE paitentid=%s",(paitentid.get(),))
            row=mycursor.fetchone()
            
            
            if row!=None:
                sqlq="""update record set paitentname=%s,paitentissue=%s,paitentcity=%s,
                paitentfee=%s,paitentgender=%s,paitentdob=%s,paitentage=%s,admitteddate=%s,
                fathername=%s,bloodgroup=%s,contactno=%s,aadharno=%s,nextvisit=%s,postcode=%s,
                bloodpressure=%s,roomno=%s,dischargedate=%s,email=%s WHERE paitentid=%s"""
                dsql=(paitentname.get(),paitentissue.get(),
                     paitentcity.get(),paitentfee.get(),paitentgender.get(),paitentdob.get(),
                     paitentage.get(),admitteddate.get(),
                     fathername.get(),bloodgroup.get(),contactno.get(),
                     aadharno.get(),nextvisit.get(),postcode.get(),bloodpressure.get(),roomno.get(),
                     dischargedate.get(),email.get(),paitentid.get())
                mycursor.execute(sqlq,dsql)
                mysqldb.commit()
                messagebox.showinfo('Info','Updated Successfully')
            else:
                messagebox.showerror("Error","Enter the proper Paitent Id")
          
            
         
        
    def display():
        lbox.delete(*lbox.get_children())
        mysqldb=mysql.connector.connect(host='localhost',port='3306',user='root',password="1436",database='hospital')
        mycursor=mysqldb.cursor()
        mycursor.execute("SELECT * FROM record")
        records=mycursor.fetchall()
        
        
        for i in records:
            lbox.insert("","end",values=i)
            mysqldb.close()
        
        
    def GetValue(event):
        cursor_row=lbox.focus()
        con=lbox.item(cursor_row)
        row=con['values']
        paitentid.set(row[0]),
        paitentname.set(row[1]),
        paitentissue.set(row[2]),
        paitentcity.set(row[3]),
        paitentfee.set(row[4]),
        paitentgender.set(row[5]),
        paitentdob.set(row[6]),
        paitentage.set(row[7]),
        admitteddate.set(row[8]),
        fathername.set(row[9]),
        bloodgroup.set(row[10]),
        contactno.set(row[11]),
        aadharno.set(row[12]),
        nextvisit.set(row[13]),
        postcode.set(row[14]),
        bloodpressure.set(row[15]),
        roomno.set(row[16]),
        dischargedate.set(row[17]),
        referenceno.set(row[18]),
        email.set(row[19])
        
        txtpesc.delete('1.0','end')
        
        txtpesc.insert(END,"PAITENT ID\t\t:"+paitentid.get()+'\n')
        txtpesc.insert(END,"PAITENT NAME\t\t:"+paitentname.get()+'\n')
        txtpesc.insert(END,"PAITENT ISSUE\t\t:"+paitentissue.get()+'\n')
        txtpesc.insert(END,"PAITENT CITY\t\t:"+paitentcity.get()+'\n')
        txtpesc.insert(END,"PAITENT FEE\t\t:"+paitentfee.get()+'\n')
        txtpesc.insert(END,"PAITENT GENDER\t\t:"+paitentgender.get()+'\n')
        txtpesc.insert(END,"PAITENT DOB\t\t:"+paitentdob.get()+'\n')
        txtpesc.insert(END,"PAITENT AGE\t\t:"+paitentage.get()+'\n')
        txtpesc.insert(END,"ADMITTED DATE\t\t:"+admitteddate.get()+'\n')
        txtpesc.insert(END,"FATHER NAME\t\t:"+fathername.get()+'\n')
        txtpesc.insert(END,"BLOOD GROUP\t\t:"+bloodgroup.get()+'\n')
        txtpesc.insert(END,"CONTACT NO\t\t:"+contactno.get()+'\n')
        txtpesc.insert(END,"AADHAR NO\t\t:"+aadharno.get()+'\n')
        txtpesc.insert(END,"NEXT VISIT\t\t:"+nextvisit.get()+'\n')
        txtpesc.insert(END,"POST CODE\t\t:"+postcode.get()+'\n')
        txtpesc.insert(END,"BLOOD PRESSURE\t\t:"+bloodpressure.get()+'\n')
        txtpesc.insert(END,"NAME OF TABLES\t\t:"+roomno.get()+'\n')
        txtpesc.insert(END,"DISCHARGE DATE\t\t:"+dischargedate.get()+'\n')
        txtpesc.insert(END,"REFERENCE NO:\t\t:"+referenceno.get()+'\n')
        txtpesc.insert(END,"EMAIL ID\t\t:"+email.get()+'\n')
        txtpesc.insert(END,"============================================"+'\n')
        
    
    root=Toplevel()
    root.title("Hospital Management System")
    root.geometry("1920x800+0+0")
    root.state('zoomed')
    root.resizable(0,0)

    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview')
    
    
    Label(root,text="HOSPITAL MANAGEMENT SYSTEM",font=("times new roman",40,'bold'),bd=20,relief=RIDGE,fg='red',bg="white").pack(side=TOP,fill=X)
    
    dframe=Frame(root,bd=20,relief=RIDGE)
    dframe.place(x=0,y=110,width=1365,height=400)
    
    dframeleft=LabelFrame(dframe,bd=10,padx=20,bg='light grey',relief=RIDGE,font=("arial",12,'bold'),text="Paitent Information")
    dframeleft.place(x=0,y=5,width=920,height=350)
    
    dframeright=LabelFrame(dframe,bd=10,bg='light grey',padx=20,relief=RIDGE,font=("arial",12,'bold'),text="Pescription")
    dframeright.place(x=930,y=5,width=390,height=290)

    #=========Time Frame===========
    tframe=LabelFrame(dframe,bd=10,bg='light grey',padx=20,relief=RIDGE,font=("arial",12,'bold'))
    tframe.place(x=930,y=295,width=390,height=65)

    clock=Label(tframe,font=("Calibri",20),bg='light grey',fg='black')
    clock.pack()

    get_time()
    
    #===========Button================
    bframe=Frame(root,bd=20,relief=RIDGE)
    bframe.place(x=0,y=510,width=940,height=70)
    
    #============Treeview frame============
    
    treeframe=Frame(root,bd=20,relief=RIDGE)
    treeframe.place(x=0,y=590,width=1365,height=150)
    
    #==============Search Frame==============
    sframe=Frame(root,bd=20,relief=RIDGE)
    sframe.place(x=941,y=510,width=425,height=70)
    
    selectinp=StringVar()
    
    comsrch=ttk.Combobox(sframe,font=("calibri",10),state="readonly",width=18,textvariable=selectinp)
    comsrch['values']=("CONTACTNO","REFERENCENO","PAITENTID")
    comsrch.place(x=2,y=5)
    comsrch.current(0)
    
    srchop=StringVar()
    
    entbox=Entry(sframe,width=29,bg='light grey',textvariable=srchop)
    entbox.place(x=160,y=5)
    
    b1=Button(sframe,text="Search",borderwidth=0,command=srch)
    b1.place(x=350,y=2)
    #===============Variable declaration===================
    
    #cols=['Paitent ID','Paitent Name','Paitent Issue','Paitent City','Paitent Fee','Paitent Gender','Paitent DOB','Paitent Age','Admitted Date'
    #     ,'Father Name','Blood Group','Contact no','Aadhar No','Next Visit','PostCode','Blood Pressure','Room No','Discharge Date','Email']
    #bsrch=Button(bframe,text="Search",width=24,padx=2,pady=6)
    #bsrch.grid(row=0,column=5)
    
    global paitentid
    global paitentname
    global paitentissue
    global paitentcity
    global paitentfee
    global paitentgender
    global paitentdob
    global paitentage
    global admitteddate
    global fathername
    global bloodgroup
    global contactno
    global aadharno
    global nextvisit
    global postcode
    global bloodpressure
    global roomno
    global dischargedate
    global referenceno
    global email
    
    paitentid=StringVar()
    paitentname=StringVar()
    paitentissue=StringVar()
    paitentcity=StringVar()
    paitentfee=StringVar()
    paitentgender=StringVar()
    paitentdob=StringVar()
    paitentage=StringVar()
    admitteddate=StringVar()
    fathername=StringVar()
    bloodgroup=StringVar()
    contactno=StringVar()
    aadharno=StringVar()
    nextvisit=StringVar()
    postcode=StringVar()
    bloodpressure=StringVar()
    roomno=StringVar()
    dischargedate=StringVar()
    referenceno=StringVar()
    email=StringVar()
    
    #===============Enter Label===============
    
    pid=Label(dframe,bg='light grey',text="Paitent ID",font=("calibri",10,))
    pid.grid(row=0,column=0,padx=20,pady=25)
    
    epid=ttk.Entry(dframe,font=("calibri",10,),textvariable=paitentid)
    epid.grid(row=0,column=1)
    
    pname=Label(dframe,bg='light grey',text="Paitent Name",font=("calibri",10))
    pname.grid(row=0,column=2,padx=20)
    
    epname=ttk.Entry(dframe,font=("calibri",10),textvariable=paitentname)
    epname.grid(row=0,column=3)
    
    pissue=Label(dframe,bg='light grey',text="Paitent Issue",font=("calibri",10))
    pissue.grid(row=0,column=4,padx=20)
    
    epissue=ttk.Entry(dframe,font=("calibri",10),textvariable=paitentissue)
    epissue.grid(row=0,column=5)
    
    pcity=Label(dframe,bg='light grey',text="Paitent City",font=("calibri",10))
    pcity.grid(row=1,column=0)
    
    epcity=ttk.Entry(dframe,font=("calibri",10),textvariable=paitentcity)
    epcity.grid(row=1,column=1)
    
    pfee=Label(dframe,bg='light grey',text="Paitent Fee",font=("calibri",10))
    pfee.grid(row=1,column=2)
    
    epfee=ttk.Entry(dframe,font=("calibri",10),textvariable=paitentfee)
    epfee.grid(row=1,column=3)
    
    pgen=Label(dframe,bg='light grey',text="Paitent Gender",font=("calibri",10))
    pgen.grid(row=1,column=4)
     
    comgen=ttk.Combobox(dframe,font=("calibri",10),state="readonly",width=18,textvariable=paitentgender)
    comgen['values']=("Select","Male","Female")
    comgen.grid(row=1,column=5)
    comgen.current(0)
    
    pdob=Label(dframe,bg='light grey',text="Paitent DOB",font=("calibri",10))
    pdob.grid(row=2,column=0)
    
    epdob=ttk.Entry(dframe,font=("calibri",10),textvariable=paitentdob)
    epdob.grid(row=2,column=1,padx=20,pady=25)
    
    page=Label(dframe,bg='light grey',text="Paitent Age",font=("calibri",10))
    page.grid(row=2,column=2)
    
    epage=ttk.Entry(dframe,font=("calibri",10),textvariable=paitentage)
    epage.grid(row=2,column=3)
    
    
    pdoa=Label(dframe,bg='light grey',text="Admitted Date",font=("calibri",10))
    pdoa.grid(row=2,column=4)
    
    epdoa=ttk.Entry(dframe,font=("calibri",10),textvariable=admitteddate)
    epdoa.grid(row=2,column=5)
    
    
    FHname=Label(dframe,bg='light grey',text="Father Name",font=("calibri",10))
    FHname.grid(row=3,column=0)
    
    eFHname=ttk.Entry(dframe,font=("calibri",10),textvariable=fathername)
    eFHname.grid(row=3,column=1)
    
    
    bgro=Label(dframe,bg='light grey',text="Blood Group",font=("calibri",10))
    bgro.grid(row=3,column=2)
    
    ebgro=ttk.Entry(dframe,font=("calibri",10),textvariable=bloodgroup)
    ebgro.grid(row=3,column=3)
    
    
    pcno=Label(dframe,bg='light grey',text="Contact no",font=("calibri",10))
    pcno.grid(row=3,column=4)

    epcno=ttk.Entry(dframe,font=("calibri",10),textvariable=contactno)
    epcno.grid(row=3,column=5)
    
    
    aano=Label(dframe,bg='light grey',text="Aadhar No",font=("calibri",10))
    aano.grid(row=4,column=0,padx=20,pady=25)

    eaano=ttk.Entry(dframe,font=("calibri",10),textvariable=aadharno)
    eaano.grid(row=4,column=1)
    
    
    nvis=Label(dframe,bg='light grey',text="Next Visit",font=("calibri",10))
    nvis.grid(row=4,column=2,padx=20,pady=25)

    envis=ttk.Entry(dframe,font=("calibri",10),textvariable=nextvisit)
    envis.grid(row=4,column=3)
    
    
    post=Label(dframe,bg='light grey',text="PostCode",font=("calibri",10))
    post.grid(row=4,column=4,padx=20,pady=25)
    
    epost=ttk.Entry(dframe,font=("calibri",10),textvariable=postcode)
    epost.grid(row=4,column=5)
    
    bpre=Label(dframe,bg='light grey',text="Blood Pressure",font=("calibri",10))
    bpre.grid(row=5,column=0,padx=10)

    ebpre=ttk.Entry(dframe,font=("calibri",10),textvariable=bloodpressure)
    ebpre.grid(row=5,column=1)
    
    tname=Label(dframe,bg='light grey',text="Tablet Name",font=("calibri",10))
    tname.grid(row=5,column=2,padx=10)

    eroomno=ttk.Entry(dframe,font=("calibri",10),textvariable=roomno)
    eroomno.grid(row=5,column=3)
    
    dod=Label(dframe,bg='light grey',text="Discharge Date",font=("calibri",10))
    dod.grid(row=5,column=4)

    edod=ttk.Entry(dframe,font=("calibri",10),textvariable=dischargedate)
    edod.grid(row=5,column=5)
    
    refno=Label(dframe,bg='light grey',text="Reference No",font=("calibri",10))
    refno.grid(row=6,column=0)

    erefno=ttk.Entry(dframe,font=("calibri",10),textvariable=referenceno)
    erefno.grid(row=6,column=1)
    
    
    lemail=Label(dframe,bg='light grey',text="Email",font=("calibri",10))
    lemail.grid(row=6,column=2)

    eemail=ttk.Entry(dframe,font=("calibri",10),width=66,textvariable=email)
    eemail.grid(row=6,column=3,columnspan=3,padx=20,pady=25)
    
    #=======Description=========
    txtpesc=Text(dframeright,font=("calibri",11),width=70,height=20,padx=2,pady=6)
    
    v1bar=ttk.Scrollbar(dframeright,orient=VERTICAL,command=txtpesc.yview)
    h1bar=ttk.Scrollbar(dframeright,orient=HORIZONTAL,command=txtpesc.xview)
    
    txtpesc.configure(yscroll=v1bar.set,xscroll=h1bar.set)
                     
                     
    v1bar.pack(side=LEFT,fill=Y)
    h1bar.pack(side=BOTTOM,fill=X)
    
    txtpesc.pack()
    
    #===========Button==============
    bpescd=Button(bframe,text="Insert Data",width=20,command=pescdata,padx=2,pady=6)
    bpescd.grid(row=0,column=1)
    
    bupd=Button(bframe,text="Update",width=20,command=update,padx=2,pady=6)
    bupd.grid(row=0,column=2)
    
    bdel=Button(bframe,text="Delete",width=20,command=deleterec,padx=2,pady=6)
    bdel.grid(row=0,column=3)
    
    bcle=Button(bframe,text="Exit",command=exits,width=20,padx=2,pady=6)
    bcle.grid(row=0,column=6)
    
    bnor=Button(bframe,text="Show records",command=display,width=20,padx=2,pady=6)
    bnor.grid(row=0,column=5)
    
     
    
    
    bexit=Button(bframe,text="Id",width=20,command=paid,padx=2,pady=6)
    bexit.grid(row=0,column=4)

    
    #===========Scroll Bar==============
    
    cols=['Paitent ID','Paitent Name','Paitent Issue','Paitent City','Paitent Fee',
           'Paitent Gender','Paitent DOB','Paitent Age','Admitted Date'
          ,'Father Name','Blood Group','Contact no','Aadhar No','Next Visit','PostCode',
          'Blood Pressure','Room No','Discharge Date','Reference No',
          'Email']
    
   
    
    
    lbox=ttk.Treeview(treeframe,columns=cols,height=5,selectmode='browse')
                     
    
    vbar=ttk.Scrollbar(treeframe,orient=VERTICAL,command=lbox.yview)
    hbar=ttk.Scrollbar(treeframe,orient=HORIZONTAL,command=lbox.xview)
    
    
    lbox.configure(yscroll=vbar.set,xscroll=hbar.set)
                     
    
    vbar.pack(side=LEFT,fill=Y)
    hbar.pack(side=BOTTOM,fill=X)
    
    
    
    lbox.heading('Paitent ID',text='Paitent ID')
    lbox.heading('Paitent Name',text='Paitent Name')
    lbox.heading('Paitent Issue',text='Paitent Issue')
    lbox.heading('Paitent City',text='Paitent City')
    lbox.heading('Paitent Fee',text='Paitent Fee')
    lbox.heading('Paitent Gender',text='Paitent Gender')
    lbox.heading('Paitent DOB',text='Paitent DOB')
    lbox.heading('Paitent Age',text='Paitent Age')
    lbox.heading('Admitted Date',text='Admitted Date')
    lbox.heading('Father Name',text='Father Name')
    lbox.heading('Blood Group',text='Blood Group')
    lbox.heading('Contact no',text='Contact no')
    lbox.heading('Aadhar No',text='Aadhar No')
    lbox.heading('Next Visit',text='Next Visit')
    lbox.heading('PostCode',text='PostCode')
    lbox.heading('Blood Pressure',text='Blood Pressure')
    lbox.heading('Room No',text='Room No')
    lbox.heading('Discharge Date',text='Discharge Date')
    lbox.heading('Reference No',text='Reference No')
    lbox.heading('Email',text='Email')

    
    lbox['show']='headings'
    
    
    lbox.column('Email',width=300)
    
    lbox.pack(fill=BOTH,expand=1)
    display()
    
    lbox.bind('<Double-Button-1>',GetValue)
    
    root.mainloop()

Hospital()

