from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
#functinality Part

def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from Student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'This {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def search_student():
     def search_data():
         query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
         mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
         studentTable.delete(*studentTable.get_children())
         fetched_data=mycursor.fetchall()
         for data in fetched_data:
             studentTable.insert('',END,'values=data')


     search_window=Toplevel()
     search_window.title('Search Student')
     search_window.grab_set()
     search_window.resizable(0,0)

     
     idLabel=Label(search_window,text='Id',font=('poppins',12))
     idLabel.grid(row=0,column=0,padx=20,pady=12,sticky=W)
     idEntry=Entry(search_window,font=('poppins',12),width=24)
     idEntry.grid(row=0,column=1,pady=12,padx=20)

     nameLabel=Label(search_window,text='Name',font=('poppins',12))
     nameLabel.grid(row=1,column=0,padx=20,pady=12,sticky=W)
     nameEntry=Entry(search_window,font=('poppins',12),width=24)
     nameEntry.grid(row=1,column=1,pady=12,padx=20)
     

     phoneLabel=Label(search_window,text='Phone',font=('poppins',12))
     phoneLabel.grid(row=2,column=0,padx=20,pady=12,sticky=W)
     phoneEntry=Entry(search_window,font=('poppins',12),width=24)
     phoneEntry.grid(row=2,column=1,pady=15,padx=20)

     emailLabel=Label(search_window,text='Email',font=('poppins',12))
     emailLabel.grid(row=3,column=0,padx=20,pady=12,sticky=W)
     emailEntry=Entry(search_window,font=('poppins',12),width=24)
     emailEntry.grid(row=3,column=1,pady=15,padx=20)

     addressLabel=Label(search_window,text='Address',font=('poppins',12))
     addressLabel.grid(row=4,column=0,padx=20,pady=12,sticky=W)
     addressEntry=Entry(search_window,font=('poppins',12),width=24)
     addressEntry.grid(row=4,column=1,pady=15,padx=20)

     genderLabel=Label(search_window,text='Gender',font=('poppins',12))
     genderLabel.grid(row=5,column=0,padx=20,pady=12,sticky=W)
     genderEntry=Entry(search_window,font=('poppins',12),width=24)
     genderEntry.grid(row=5,column=1,pady=15,padx=20)

     dobLabel=Label(search_window,text='D.O.B',font=('poppins',12))
     dobLabel.grid(row=6,column=0,padx=20,pady=12,sticky=W)
     dobEntry=Entry(search_window,font=('poppins',12),width=24)
     dobEntry.grid(row=6,column=1,pady=15,padx=20)

     search_student_button=ttk.Button(search_window,text='SEARCH',width=30,command=search_data)
     search_student_button.grid(row=8,column=1,pady=20)


def add_student():
     def add_data():
        if idEntry.get()=='' or  nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All Fields are required',parent=add_window)

        else:
            currentdate = time.strftime('%D/%m/%Y')
            currenttime = time.strftime('%H:%M:%S')
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                                        genderEntry.get(),dobEntry.get(),currentdate,currenttime))
                con.commit()
                result=messagebox.askquestion('Confirm','Data added successfully. Do you want to clean the form?',parent=add_window)
                if  result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','ID cannot be repeated',parent=add_window)
                return

            query='select *from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:               
                studentTable.insert('',END,values=data)
            

     add_window=Toplevel()
     add_window.grab_set()
     add_window.resizable(0,0)

     
     idLabel=Label(add_window,text='Id',font=('poppins',12))
     idLabel.grid(row=0,column=0,padx=20,pady=12,sticky=W)
     idEntry=Entry(add_window,font=('poppins',12),width=24)
     idEntry.grid(row=0,column=1,pady=12,padx=20)

     nameLabel=Label(add_window,text='Name',font=('poppins',12))
     nameLabel.grid(row=1,column=0,padx=20,pady=12,sticky=W)
     nameEntry=Entry(add_window,font=('poppins',12),width=24)
     nameEntry.grid(row=1,column=1,pady=12,padx=20)
     

     phoneLabel=Label(add_window,text='Phone',font=('poppins',12))
     phoneLabel.grid(row=2,column=0,padx=20,pady=12,sticky=W)
     phoneEntry=Entry(add_window,font=('poppins',12),width=24)
     phoneEntry.grid(row=2,column=1,pady=15,padx=20)

     emailLabel=Label(add_window,text='Email',font=('poppins',12))
     emailLabel.grid(row=3,column=0,padx=20,pady=12,sticky=W)
     emailEntry=Entry(add_window,font=('poppins',12),width=24)
     emailEntry.grid(row=3,column=1,pady=15,padx=20)

     addressLabel=Label(add_window,text='Address',font=('poppins',12))
     addressLabel.grid(row=4,column=0,padx=20,pady=12,sticky=W)
     addressEntry=Entry(add_window,font=('poppins',12),width=24)
     addressEntry.grid(row=4,column=1,pady=15,padx=20)

     genderLabel=Label(add_window,text='Gender',font=('poppins',12))
     genderLabel.grid(row=5,column=0,padx=20,pady=12,sticky=W)
     genderEntry=Entry(add_window,font=('poppins',12),width=24)
     genderEntry.grid(row=5,column=1,pady=15,padx=20)

     dobLabel=Label(add_window,text='D.O.B',font=('poppins',12))
     dobLabel.grid(row=6,column=0,padx=20,pady=12,sticky=W)
     dobEntry=Entry(add_window,font=('poppins',12),width=24)
     dobEntry.grid(row=6,column=1,pady=15,padx=20)

     add_student_button=ttk.Button(add_window,text='ADD STUDENT',width=30,command=add_data)
     add_student_button.grid(row=8,column=1,pady=20)
     

def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='pravin')
            mycursor=con.cursor()
            
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectwindow)
            return 

        try:
                query='create database studentmanagementsystem'   
                mycursor.execute(query)
                query='use studentmanagementsystem'
                mycursor.execute(query)
                query='create table student(id int not null primary key, name varchar(30), mobile varchar(10),email varchar(30),address varchar(100),gender varchar(14),dob varchar(20),date varchar(50),time varchar(50))'
                mycursor.execute(query)

        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection Is Successful',parent=connectwindow)
        connectwindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)


    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('500x300+700+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)

    hostnameLabel=Label(connectwindow,text='Host Name',font=('poppins',16))
    hostnameLabel.grid(row=0,column=0,padx=40,pady=20)

    hostEntry=Entry(connectwindow,font=('poppins',15),bd=2)
    hostEntry.grid(row=0,column=1,padx=30,pady=20)

    usernameLabel=Label(connectwindow,text='User Name',font=('poppins',16))
    usernameLabel.grid(row=1,column=0,padx=40)

    usernameEntry=Entry(connectwindow,font=('poppins',15),bd=2)
    usernameEntry.grid(row=1,column=1,padx=30,pady=20)

    passwordLabel=Label(connectwindow,text='Password',font=('poppins',16))
    passwordLabel.grid(row=2,column=0,padx=40)

    passwordEntry=Entry(connectwindow,font=('poppins',15),bd=2)
    passwordEntry.grid(row=2,column=1,padx=30,pady=20)

    connectButton=ttk.Button(connectwindow,text='CONNECT',command=connect)  
    connectButton.grid(row=3,column=1)


 

def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'        Date: {date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)
    

#GUI Part

root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('breeze')

root.geometry('1640x1080+120+0')
root.resizable(0,0)
root.title('SIBT Student Information Management System')

datetimeLabel=Label(root,text='hello',font=('poppins',18))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Information Managment System' #s[count]=t when count is 1
sliderLabel=Label(root,text=s,font=('poppins',28,'bold'))
sliderLabel.place(x=500,y=20)

connectButton=ttk.Button(root,text='Connect to Database',command=connect_database)
connectButton.place(x=1400,y=30)

leftFrame=Frame(root)
leftFrame.place(x=100,y=170,width=500,height=800,)

logo_image=PhotoImage(file='student.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=30,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)


searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=30,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)


deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=30,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=30,state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=20)


showstudentButton=ttk.Button(leftFrame,text='Show Student',width=30,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)


exportstudentButton=ttk.Button(leftFrame,text='Export Student',width=30,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)


exitstudentButton=ttk.Button(leftFrame,text='Exit Student',width=30)
exitstudentButton.grid(row=7,column=0,pady=20)


rightFrame=Frame(root)
rightFrame.place(x=500,y=170,width=1100,height=800,)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)



studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile No','Email','Address','Gender',
                                 'D.O.B','Added Date'),                   
                         xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)




scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)



studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date ')

studentTable.config(show='headings')



root.mainloop() 