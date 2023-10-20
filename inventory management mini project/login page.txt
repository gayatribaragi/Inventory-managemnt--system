import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")



        # ===left_menu===
        self.phone_image = Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojinvent\images\phone_image.jpg")
        self.phone_image = self.phone_image.resize((330, 450))
        self.phone_image = ImageTk.PhotoImage(self.phone_image)

        self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0, relief=RAISED)
        self.lbl_phone_image.place(x=200, y=90)

        #=========login frame======

        self.emploee_id = StringVar()
        self.passdword = StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_employee=Label(login_frame,text="Employee Id",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)


        txt_employee=Entry(login_frame,textvariable=self.emploee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50,
                                                                                                             y=200)
        txt_pass = Entry(login_frame,textvariable=self.passdword,show="*", font=("times new roman", 15), bg="#ECECEC").place(x=50, y=240, width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Roundeed MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        hr=Label(login_frame,bg="lightgray").place(x=50,y=140,width=250,height=2)






    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.emploee_id.get()=="" or self.passdword.get()=="":
                messagebox.showerror('Error',"All fields are required",parent=self.root)
            else:
                cur.execute("Select utype from employee where eid=? AND password=?",(self.emploee_id.get(),self.passdword.get()))
                user = cur.fetchone()
                if user==None:
                    messagebox.showerror('Error', "Invalid Username/password", parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)





root = Tk()
obj = Login_System(root)
root.mainloop()