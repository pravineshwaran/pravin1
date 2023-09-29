from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='pravin' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
        
        
    else:
        messagebox.showerror('Error','Please check inputs')

window=Tk()
window.title('Login to Student Information Management System')

window.geometry('1800x1000+40+0')

window.resizable(0,0)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=-800,y=-300)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=600,y=200)

logoImage=PhotoImage(file='logo.png')

LogoLable=Label(loginFrame,image=logoImage)
LogoLable.grid(row=0,column=0,columnspan=2,pady=40)
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='User Name', compound=LEFT
                    ,font=('poppins',16,),bg='white',fg='grey')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('poppins',16,),bd=2,fg='grey')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password', compound=LEFT
                    ,font=('poppins',16,),bg='white',fg='grey')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('poppins',16,),bd=2,fg='grey')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('poppins',12),width=25
                   ,fg='white',bg='royalblue',activebackground='royalblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=4,column=1,pady=20)



window.mainloop()