from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector as mysql
mydb=mysql.connect(
    host="localhost",
    user="root",
    passwd="9457012141",
    database="rgipt_entry"
)
mycursor=mydb.cursor()
mycursor.execute("show tables")
tables=mycursor.fetchall()
if not tables:                                             
    mycursor=mydb.cursor()
    mycursor.execute("create table welcome_to_rgipt(Gatepass_ID int primary key,Name varchar(45),Phone_Number varchar(15),Enter_or_Exit varchar(15),Time_of_Enter_or_Exit varchar(20),Date varchar(15))")
else:    
    if ("welcome_to_rgipt",) not in tables:
        mycursor=mydb.cursor()
        mycursor.execute("create table welcome_to_rgipt(Gatepass_ID int primary key,Name varchar(45),Phone_Number varchar(15),Enter_or_Exit varchar(15),Time_of_Enter_or_Exit varchar(20),Date varchar(15))")
    else:
        pass
mycursor=mydb.cursor()
mycursor.execute("show tables")
tables=mycursor.fetchall()
if not tables:
    mycursor=mydb.cursor()
    mycursor.execute("create table employee(E_ID varchar(20) primary key,User_Name varchar(20) not null,Password varchar(30) not null)")
    s="insert into employee(E_ID,User_Name,Password) values(%s,%s,%s)"
    b1=("12112","Ram Kishan","456")
    mycursor.execute(s,b1)
    mycursor.execute("commit")
    b2=("13228","Satyendra Singh","7458854")
    mycursor.execute(s,b2)
    mycursor.execute("commit")
    b3=("15448","Kishore Verma","5693312")
    mycursor.execute(s,b3)
    mycursor.execute("commit")
else:    
    if ("employee",) not in tables:
        mycursor=mydb.cursor()
        mycursor.execute("create table employee(E_ID varchar(20) primary key,User_Name varchar(20) not null,Password varchar(30) not null)")
        s="insert into employee(E_ID,User_Name,Password) values(%s,%s,%s)"
        b1=("12112","Ram Kishan","456")
        mycursor.execute(s,b1)
        mycursor.execute("commit")
        b2=("13228","Satyendra Singh","7458854")
        mycursor.execute(s,b2)
        mycursor.execute("commit")
        b3=("15448","Kishore Verma","5693312")
        mycursor.execute(s,b3)
        mycursor.execute("commit")
    else:
        pass

def openwindow():
    def insert():
        id=e_id.get()
        name=e_name.get()
        phone=e_phone.get()
        enter=e_enter.get()
        time=e_time.get()
        date=e_date.get()
        if(id=="" or name=="" or phone=="" or enter=="" or time=="" or date==""):
            messagebox.showinfo("Insert Status", "All fields are required")
        else:
            con=mysql.connect(host="localhost",user="root",password="9457012141",database="rgipt_entry")
            cursor=con.cursor()
            cursor.execute("insert into welcome_to_rgipt values('"+id+"','"+ name +"','"+ phone +"','"+ enter +"','"+ time +"','"+ date +"')")
            cursor.execute("commit")
            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_phone.delete(0,'end')
            e_enter.delete(0,'end')
            e_time.delete(0,'end')
            e_date.delete(0,'end')
            messagebox.showinfo("Insert Status","Inserted Successfully")
            con.close()

    def delete():
        if(e_id.get()==""):
            messagebox.showinfo("Delete Status","ID is compulsory for Delete")
        else:
            con=mysql.connect(host="localhost",user="root",password="9457012141",database="rgipt_entry")
            cursor=con.cursor()
            cursor.execute("delete from welcome_to_rgipt where Gatepass_ID='"+e_id.get()+"'")
            cursor.execute("commit")
            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_phone.delete(0,'end')
            e_enter.delete(0,'end')
            e_time.delete(0,'end')
            e_date.delete(0,'end')
            messagebox.showinfo("Delete Status","Deleted Successfully")
            con.close()

    def update():
        id=e_id.get()
        name=e_name.get()
        phone=e_phone.get()
        enter=e_enter.get()
        time=e_time.get()
        date=e_date.get()
        if(id=="" or name=="" or phone=="" or enter=="" or time=="" or date==""):
            messagebox.showinfo("Insert Status", "All fields are required")
        else:
            con=mysql.connect(host="localhost",user="root",password="9457012141",database="rgipt_entry")
            cursor=con.cursor()
            cursor.execute("update welcome_to_rgipt set Name='"+ name +"',Phone_Number='"+ phone +"',Enter_or_Exit='"+ enter +"',Time_of_Enter_or_Exit='"+ time +"',Date='"+ date +"' where Gatepass_ID='"+ id +"'")
            cursor.execute("commit")
            e_id.delete(0,'end')
            e_name.delete(0,'end')
            e_phone.delete(0,'end')
            e_enter.delete(0,'end')
            e_time.delete(0,'end')
            e_date.delete(0,'end')
            messagebox.showinfo("Update Status","Updated Successfully")
            con.close()

    def show():
        con=mysql.connect(host="localhost",user="root",password="9457012141",database="rgipt_entry")
        cursor=con.cursor()
        cursor.execute("select * from welcome_to_rgipt")
        rows=cursor.fetchall()
        for row in rows:
            insertData=str(row[0])+'     '+row[1]+'      '+row[3]
            list.insert(list.size()+1,insertData)
        con.close()

    def get():
        if(e_id.get()==""):
            messagebox.showinfo("Fetch Status", "GATEPASS ID is required")
        else:
            con=mysql.connect(host="localhost",user="root",password="9457012141",database="rgipt_entry")
            cursor=con.cursor()
            cursor.execute("select * from welcome_to_rgipt where Gatepass_ID='"+e_id.get()+"'")
            rows=cursor.fetchall()
            for row in rows:
                e_name.insert(0,row[1])
                e_phone.insert(0,row[2])
                e_enter.insert(0,row[3])
                e_time.insert(0,row[4])
                e_date.insert(0,row[5])
            con.close();
        
    def clear():
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        e_enter.delete(0,'end')
        e_time.delete(0,'end')
        e_date.delete(0,'end')
    

    new_window=Toplevel(root)
    new_window.geometry("800x500")
    new_window.title("Python+Tkinter+MySql")
    new_window.resizable(False,False)
    bg=PhotoImage(file="dsc-0020.png")
    my_label=Label(new_window,image=bg)
    my_label.place(x=0,y=0,relwidth=1, relheight=1)
    head=Label(new_window, text='Welcome to RGIPT', font=('Bold',20))
    head.pack(pady=50)
    id=Label(new_window, text='Gatepass Number:', font=('Bell MT',15))
    id.pack(pady=50)
    id.place(x=20,y=90)
    name=Label(new_window, text='Name:', font=('Bell MT',15))
    name.pack(pady=50)
    name.place(x=20,y=120)
    phone=Label(new_window, text='Phone Number:', font=('Bell MT',15))
    phone.pack(pady=50)
    phone.place(x=20,y=150)
    Exit=Label(new_window, text='Enter/Exit:', font=('Bell MT',15))
    Exit.pack(pady=50)
    Exit.place(x=20,y=180)
    Time=Label(new_window, text='Time of exit/enter:', font=('Bell MT',15))
    Time.pack(pady=50)
    Time.place(x=20,y=210)
    Date=Label(new_window, text='Date:', font=('Bell MT',15))
    Date.pack(pady=50)
    Date.place(x=20,y=240)
    e_id=Entry(new_window)
    e_id.pack(pady=50)
    e_id.place(x=300,y=90)
    e_name=Entry(new_window)
    e_name.pack(pady=50)
    e_name.place(x=300,y=120)
    e_phone=Entry(new_window)
    e_phone.pack(pady=50)
    e_phone.place(x=300,y=150)
    e_enter=Entry(new_window)
    e_enter.pack(pady=50)
    e_enter.place(x=300,y=180)
    e_time=Entry(new_window)
    e_time.pack(pady=50)
    e_time.place(x=300,y=210)
    e_date=Entry(new_window)
    e_date.pack(pady=50)
    e_date.place(x=300,y=240)
    insert=Button(new_window,text="insert",font=("bold",10),bg="white",command=insert)
    insert.place(x=100,y=300)
    delete=Button(new_window,text="delete",font=("bold",10),bg="white",command=delete)
    delete.place(x=150,y=300)
    update=Button(new_window,text="update",font=("bold",10),bg="white",command=update)
    update.place(x=200,y=300)
    get=Button(new_window,text="get",font=("bold",10),bg="white",command=get)
    get.place(x=260,y=300)
    clear=Button(new_window,text="clear",font=("bold",10),bg="white",command=clear)
    clear.place(x=300,y=300)
    list=Listbox(new_window)
    list.place(x=550,y=90)
    show()
    new_window.mainloop()
    
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1196x600+100+50")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="index.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)

        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)

        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forget Password/Username?",bg="white",fg="#d77337",bd=0,font=("times new roman",12),command=self.forget).place(x=90,y=280)
        login_btn=Button(self.root,text="Login",fg="white",bg="#d77337",font=("times new roman",20),command=self.login_function).place(x=300,y=470,width=180,height=40)

    def forget(self):
        self.root1=Toplevel()
        self.root1.title=("Forget Password")
        self.root1.geometry("800x400+450+150")
        self.root1.resizable(False,False)
        self.root1.focus_force()
        self.root1.grab_set()
        self.root1.bg=ImageTk.PhotoImage(file="index.png")
        self.root1.bg_image=Label(self.root1,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root1,bg="white")
        Frame_login.place(x=0,y=0,height=340,width=500)

        title=Label(Frame_login,text="Forget Password",font=("Impact",35,"bold"),fg="#055BB5",bg="white").place(x=90,y=5)
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",13,"bold"),fg="gray",bg="white").place(x=90,y=80)

        self.usern=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.usern.place(x=90,y=110,width=350,height=35)
        lbl_id=Label(Frame_login,text="Employee ID",font=("Goudy old style",13,"bold"),fg="gray",bg="white").place(x=90,y=150)

        self.ids=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.ids.place(x=90,y=180,width=350,height=35)
        lbl_newpass=Label(Frame_login,text="New Password",font=("Goudy old style",13,"bold"),fg="gray",bg="white").place(x=90,y=220)

        self.new_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.new_pass.place(x=90,y=250,width=350,height=35)
        reset_btn=Button(self.root1,text="Reset",fg="white",bg="#055BB5",font=("times new roman",20),command=self.forgot_function).place(x=170,y=300,width=180,height=40)
        
    def forgot_function(self):
        mycursor=mydb.cursor()
        mycursor.execute("select E_ID from employee")
        tuples=mycursor.fetchall()
        emp_idds=self.ids.get()
        usernnn=self.usern.get()
        if not tuples:
            messagebox.showerror(title='Error', message="Employee not found in the database")
        else:
            if (emp_idds,) in tuples:
                    password=self.new_pass.get()
                    emp_ids=self.ids.get()
                    user_n=self.usern.get()
                    mycursor=mydb.cursor()
                    mycursor.execute("update employee set User_Name='"+user_n+"',Password='"+ password +"' where E_ID='"+emp_ids+"'")
                    messagebox.showinfo(title='Info', message="Password is resetted")
                    mycursor.execute("commit")

                    

            else:
                messagebox.showerror(title='Error', message="Employee not found in the database")


    def login_function(self):
        mycursor=mydb.cursor()
        mycursor.execute("select Password,User_Name from employee")
        tuples=mycursor.fetchall()
        res=((self.txt_pass.get()),(self.txt_user.get()))
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            print(tuples[0])

        else:
                if res not in tuples:
                    messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
                else:  
                    openwindow()          




root=Tk()
obj=Login(root)
root.mainloop()
