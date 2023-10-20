from tkinter import *
from PIL  import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==========================
        # All Variables======
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_conatct = StringVar()
        self.var_description = StringVar()


        #======search frame============

        #=======options=======
        lbl_search=Label(self.root,text="Invoice No",bg="white",font=("goudy old style",15))
        lbl_search.place(x=700,y=80)


        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=800,y=80,width=150)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)

        #======title======
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

        #=======content=====
        #========row1=======
        lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="white").place(x=50,y=80)

        txt_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=80,width=180)

        # ========row2=======
        lbl_name=Label(self.root,text="name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name = Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=120,width=180)

        # ========row3=======
        lbl_contact=Label(self.root,text="contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
        txt_email = Entry(self.root,textvariable=self.var_conatct, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=160,width=180)

        # ========row4=======
        lbl_descrption=Label(self.root,text="description",font=("goudy old style",15),bg="white").place(x=50,y=200)
        self.txt_description = Text(self.root,font=("goudy old style", 15), bg="lightyellow")
        self.txt_description.place(x=180, y=200,width=470,height=120)

        #===buttons=====
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=180,y=370,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=300,y=370,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=420,y=370,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=540,y=370,width=110,height=35)

        # ======employee details=======
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=700, y=120, width=380, height=350)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact","description"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="invoice No")
        self.SupplierTable.heading("name", text="name")
        self.SupplierTable.heading("contact", text="contact")
        self.SupplierTable.heading("description", text="description")
        self.SupplierTable["show"]="headings"
        self.SupplierTable.column("invoice", width=90)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("description", width=100)
        self.SupplierTable .pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#========================================================================================================

    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error1","invoice Must be required",parent=self.root)
            else:
                cur.execute("Select * from Supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error2","This invoice No already assigned ,try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,description) values(?,?,?,?)",(
                       self.var_sup_invoice.get(),
                       self.var_name.get(),
                       self.var_conatct.get(),
                       self.txt_description.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error3",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error3", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']
        # print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_conatct.set(row[2]),
        self.txt_description.delete('1.0', END),
        self.txt_description.insert(END,row[3]),

    def update(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error1","invoice No Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error2","Invalid invoice",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,description=? where invoice=?",(
                       self.var_name.get(),
                       self.var_conatct.get(),
                       self.txt_description.get('1.0',END),
                       self.var_sup_invoice.get()

                                ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error3",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error1","invoice No Must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error2","Invalid invoice No",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","supplier deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error3",f"Error due to : {str(ex)}",parent=self.root)
    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_conatct.set(""),
        self.txt_description.delete('1.0', END),
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","invoice No should be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error3", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()