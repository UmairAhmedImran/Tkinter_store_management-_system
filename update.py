from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("Database/shopingmall.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) FROM inventory")

for r in result:
    id = r[0]
def labels(self, master, text, font, x, y):
    var = Label(master, text=text, font=font)
    var.place(x=x, y=y)
class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.heading = labels(self, master, "Update the database", 'arial 40 bold', 500, 0)

        self.id_le = labels(self, master, "Enter ID", 'araial 18 bold', 0, 80)

        self.id_leb = Entry(master, width=10, font='arial 18 bold')
        self.id_leb.place(x=380, y=80)

        self.btn_search = Button(master, width=15, height=2, text="Search", bg="orange", command=self.search)
        self.btn_search.place(x=550, y=80)

        self.name_l = labels(self, master, "Enter Product Name", 'arial 18 bold', 0, 150)

        self.stock_l = labels(self, master, "Enter Stock", 'arial 18 bold', 0, 220)

        self.cp_l = labels(self, master, "Enter Cost Price", 'arial 18 bold', 0, 290)

        self.sp_l = labels(self, master, "Enter Selling Price", 'arial 18 bold', 0, 360)

        self.totalcp_l = labels(self, master, "Enter Total Cost Price", 'arial 18 bold', 0, 430)

        self.totalsp_l = labels(self, master, "Enter Total Selling Price", 'arial 18 bold', 0, 500)


        self.vendor_l = labels(self, master, "Enter Vendor Name", 'arial 18 bold', 0, 570)

        self.vendor_phone_no_l = labels(self, master, "Enter Vendor Phone No.", 'arial 18 bold', 0, 630)


        self.name_e = Entry(master, width=25, font='arial 18 bold')
        self.name_e.place(x=380, y=150)

        self.stock_e = Entry(master, width=25, font='arial 18 bold')
        self.stock_e.place(x=380, y=220)

        self.cp_e = Entry(master, width=25, font='arial 18 bold')
        self.cp_e.place(x=380, y=290)

        self.sp_e = Entry(master, width=25, font='arial 18 bold')
        self.sp_e.place(x=380, y=360)

        self.totalcp_e = Entry(master, width=25, font='arial 18 bold')
        self.totalcp_e.place(x=380, y=430)

        self.totalsp_e = Entry(master, width=25, font='arial 18 bold')
        self.totalsp_e.place(x=380, y=500)

        self.vendor_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_e.place(x=380, y=570)

        self.vendor_phone_no_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_phone_no_e.place(x=380, y=630)


        self.update_button = Button(master, text="Update database", width=25, height=2, bg='steelblue', fg='white', command=self.update)
        self.update_button.place(x=550, y=700)


        self.t_box = Text(master, width=80, height=25)
        self.t_box.place(x=800, y=80)
        self.t_box.insert(END, "ID has reached upto " + str(id))

    def search(self, *args, **kwargs):
        sql = "SELECT * From inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
        conn.commit()

        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.vendor_e.delete(0, END)
        self.vendor_e.insert(0, str(self.n8))

        self.vendor_phone_no_e.delete(0, END)
        self.vendor_phone_no_e.insert(0, str(self.n9))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n5))

        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n6))

    def update(self, *args, **kwargs):
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_no_e.get()

        query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phoneno=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Update Database Successfully")



root = Tk()
b = Database(root)

root.geometry("1530x790+0+0")
root.title("Update the database")

root.mainloop()
