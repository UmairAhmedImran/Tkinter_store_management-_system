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

        self.heading = labels(self, master, "Add to the database", 'arial 40 bold', 500, 0)


        self.name_l = labels(self, master, "Enter Product Name", 'arial 18 bold', 0, 80)

        self.stock_l = labels(self, master, "Enter Stock", 'arial 18 bold', 0, 150)

        self.cp_l = labels(self, master, "Enter Cost Price", 'arial 18 bold', 0, 220)

        self.sp_l = labels(self, master, "Enter Selling Price", 'arial 18 bold', 0, 290)

        self.vendor_l = labels(self, master, "Enter Vendor Name", 'arial 18 bold', 0, 360)

        self.vendor_phone_no_l = labels(self, master, "Enter Vendor Phone No.", 'arial 18 bold', 0, 430)

        self.id_l = labels(self, master, "Enter ID", 'arial 18 bold', 0, 500)

        self.name_e = Entry(master, width=25, font='arial 18 bold')
        self.name_e.place(x=380, y=80)

        self.stock_e = Entry(master, width=25, font='arial 18 bold')
        self.stock_e.place(x=380, y=150)

        self.cp_e = Entry(master, width=25, font='arial 18 bold')
        self.cp_e.place(x=380, y=220)

        self.sp_e = Entry(master, width=25, font='arial 18 bold')
        self.sp_e.place(x=380, y=290)

        self.vendor_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_e.place(x=380, y=360)

        self.vendor_phone_no_e = Entry(master, width=25, font='arial 18 bold')
        self.vendor_phone_no_e.place(x=380, y=430)

        self.id_e = Entry(master, width=25, font='arial 18 bold')
        self.id_e.place(x=380, y=500)

        self.add_button = Button(master, text="Add to database", width=25, height=2, bg='steelblue', fg='white', command=self.get_items)
        self.add_button.place(x=550, y=580)

        self.clear_button = Button(master, text="Clear all text", width=18, height=2, bg='lightgreen', fg='white',
                                 command=self.clear_all)
        self.clear_button.place(x=380, y=580)

        self.t_box = Text(master, width=80, height=25)
        self.t_box.place(x=800, y=80)
        self.t_box.insert(END, "ID has reached upto " + str(id))

    def get_items(self, *args, **kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone_no = self.vendor_phone_no_e.get()

        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error", "Please full all of the information.")
        else:
            sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES (?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone_no))
            conn.commit()

            self.t_box.insert(END, "\n\nInserted " + str(self.name) + " into the database with code " + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_no_e.delete(0, END)
        self.id_e.delete(0, END)
root = Tk()
b = Database(root)

root.geometry("1530x790+0+0")
root.title("Add to the database")

root.mainloop()
