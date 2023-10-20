import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import billClass
from tkinter import ttk,messagebox
import sqlite3
import os
import time
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        # ===title===
        title = Label(self.root, text="Inventory Management System",font=("times new roman", 40, "bold"), bg="#010c48",fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        btn_logout = Button(self.root, text="Logout", command=self.logout,font=("times new roman", 15, "bold"), bg="yellow",cursor="hand2").place(x=1150, y=10, height=47, width=170)

        self.lbl_clock = Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH-MM-SS",font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ===left_menu===
        self.MenuLogo = Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojinvent\images\invent.jpg")
        self.MenuLogo = self.MenuLogo.resize((200, 200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=533)

        lbl_MenuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP, fill=X)

        btn_employee = Button(LeftMenu, text="Employee",command=self.employee, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="supplier",command=self.supplier, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Category = Button(LeftMenu, text="Category",command=self.category, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="product",command=self.product, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_billing = Button(LeftMenu, text="Billing",command=self.billing, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="sales", command=self.sales,font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)

        self.lbl_employee = Label(self.root, text="Total Employee\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total supplier\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_Category = Label(self.root, text="Total Category\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_Category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total product\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                 font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total sales\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                               font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # ===Footer===
        lbl_footer = Label(self.root,text="Inventory Management System \nif any queries contact 953*****89 or ga****@gmail.com",font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        self.update_content()
        # =======================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)


    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = billClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total products\n[{str(len(product))}]")

            cur.execute("Select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f"Total suppliers\n[{str(len(supplier))}]")

            cur.execute("Select * from category")
            category = cur.fetchall()
            self.lbl_Category.config(text=f"Total categories\n[{str(len(category))}]")

            cur.execute("Select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f"Total employees\n[{str(len(employee))}]")
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f"total sales[{str((bill))}]")

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"error due to : {str(ex)}",parent=self.root)

    def logout(self):
        os.system("python login.py")

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()