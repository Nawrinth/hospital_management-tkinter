from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector as sql

def forget():
    def fpwd():
        con=sql.connect(host='localhost',user='root',passwd='1436',database='hospital')
        cursor=con.cursor()
        cursor.execute('SELECT * FROM REGISTER WHERE EMAIL=%s',(e.get(),))
        row=cursor.fetchone()
        if row==None:
            messagebox.showerror("Error","There is no such Email in database")
        elif e.get()=='':
            messagebox.showerror('Error','Enter the Email')
        elif sq.get()=='Select':
            messagebox.showerror('Error','enter the proper question')
        elif sa.get()=='':
            messagebox.showerror('Error','Enter the Security Answer')
        elif np.get()=='':
            messagebox.showerror('Error','Enter the New Password')
        else:
            cursor.execute('SELECT * FROM REGISTER WHERE EMAIL=%s AND SECURITYQ=%s AND SECURITYA=%s',
            (e.get(),sq.get(),sa.get()))
            qwe=cursor.fetchone()
            if qwe==None:
                messagebox.showerror('Error','Wrong Question Or Answer')
            else:
                cursor.execute('UPDATE REGISTER SET PASSWORD=%s WHERE EMAIL=%s',(np.get(),e.get()))
                con.commit()
                messagebox.showinfo("Info",'Password Reset Successfully')

        

    root=Toplevel()
    root.geometry('340x550')
    global e
    global sq
    global sa
    global np

    #Variable
    e=StringVar()
    sq=StringVar()
    sa=StringVar()
    np=StringVar()

    Label(root,text="Forget Password",font=("times new roman",20,'bold'),fg='red',bg='white').place(x=0,y=0,relwidth=1)
    
    #email
    Label(root,text='Email',font=('times new roman',15)).place(x=10,y=60)
    eemail=Entry(root,textvariable=e,width=32,font=('times new roman',15),bg='light grey')
    eemail.place(x=10,y=100,width=300,height=30)

    #Security Question
    Label(root,text='Security Question',font=('Times new roman',15)).place(x=10,y=150)

    combo_secques=ttk.Combobox(root,font=("times new roman",15),state="readonly",textvariable=sq)
    combo_secques['values']=("Select","Your Birth Place","Your Pet Name","Favourite Actor")
    combo_secques.place(x=10,y=200,width=300)
    combo_secques.current(0)

    #Security answer
    Label(root,text='Security Answer',font=('Times new roman',15)).place(x=10,y=250)

    sa=Entry(root,textvariable=sa,font=('Times new roman',15),bg='light grey')
    sa.place(x=10,y=300,width=300,height=30)


    #New Password
    Label(root,text='New Password',font=('Times new roman',15)).place(x=10,y=350)

    p=Entry(root,textvariable=np,width=32,bg='Light Grey',font=('Times new roman',15))
    p.place(x=10,y=400,width=300,height=30)

    #Button
    btn=Button(root,text='RESET',command=fpwd,font=('Times new roman',15),bg='green',activebackground='green')
    btn.place(x=120,y=450)

    root.mainloop()
