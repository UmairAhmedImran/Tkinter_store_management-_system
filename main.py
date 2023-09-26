from tkinter import *
import tkinter.messagebox
import sqlite3
import datetime
import os
import random
import math

conn = sqlite3.connect("Database/shopingmall.db")
c = conn.cursor()

date = datetime.datetime.now().date()

products_list = []
products_price = []
products_quantity = []
products_id = []

labels_list =[]
class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.left = Frame(master, width=900, height=790, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=630, height=790, bg='lightblue')
        self.right.pack(side=RIGHT)

        self.heading  = Label(self.left, text="Micheal General Store", font="arial 40 bold", bg='white')
        self.heading.place(x=0, y=0)

        self.date_l = Label(self.right, text="Today's Date: " + str(date), font="arial 16 bold", fg='white', bg='lightblue')
        self.date_l.place(x=0, y=0)

        self.tproduct = Label(self.right, text="Products", font="arial 18 bold", bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=70)

        self.tquantity = Label(self.right, text="Quantity", font="arial 18 bold", bg='lightblue', fg='white')
        self.tquantity.place(x=250, y=70)

        self.tamount = Label(self.right, text="Amount", font="arial 18 bold", bg='lightblue', fg='white')
        self.tamount.place(x=500, y=70)

        self.enterid = Label(self.left, text="Enter Product's ID", font="arial 18 bold", bg='white')
        self.enterid.place(x=0, y=100)

        self.enteride = Entry(self.left, width=25, font="arial 18 bold", bg="lightblue")
        self.enteride.place(x=220, y=100)
        self.enteride.focus()

        self.btn_seacrh = Button(self.left, text="Search", width=25, height=2, bg='orange', command=self.ajax)
        self.btn_seacrh.place(x=300, y=150)

        self.product = Label(self.left, text="", font='arial 27 bold', bg='white', fg='steelblue')
        self.product.place(x=0, y=270)

        self.pprice = Label(self.left, text="", font='arial 27 bold', bg='white', fg='steelblue')
        self.pprice.place(x=0, y=310)

        self.total_l = Label(self.right, text="", font="arial 40 bold", bg="lightblue", fg="white")
        self.total_l.place(x=0, y=650)

        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.add_to_cart)
        self.master.bind("<space>", self.generate_bills)

    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id,))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]

        self.product.configure(text="Product's Name: " + str(self.get_name))
        self.pprice.configure(text="Price= $ " + str(self.get_price))

        self.quantity_l = Label(self.left, text="Enter Quantity:", font="arial 18 bold", bg='white')
        self.quantity_l.place(x=0, y=390)

        self.quantity_e = Entry(self.left, width=25, font="arial 18 bold", bg='lightblue')
        self.quantity_e.place(x=220, y=390)
        self.quantity_e.focus()

        self.discount_l = Label(self.left, text="Enter Discount:", font="arial 18 bold", bg='white')
        self.discount_l.place(x=0, y=430)

        self.discount_e = Entry(self.left, width=25, font="arial 18 bold", bg='lightblue')
        self.discount_e.place(x=220, y=430)
        self.discount_e.insert(END, 0)

        self.add_to_cart_button = Button(self.left, text="Add to cart", width=22, height=2, bg='orange', command=self.add_to_cart)
        self.add_to_cart_button.place(x=320, y=480)

        self.change_l = Label(self.left, text="Given Amount", font="arial 18 bold", bg="white")
        self.change_l.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, font="arial 18 bold", bg="lightblue")
        self.change_e.place(x=220, y=550)

        self.change_btn = Button(self.left, text="Calculate Change", width=22, height=2, bg='orange', command=self.change_func)
        self.change_btn.place(x=320, y=590)

        self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg='red', fg='white', command=self.generate_bills)
        self.bill_btn.place(x=80, y=680)

    def add_to_cart(self, *args, **kwargs):
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many products in our inventory.")
        else:
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - float(self.discount_e.get())
            products_list.append(self.get_name)
            products_price.append(self.final_price)
            products_quantity.append(self.quantity_value)
            products_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 120
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font="arial 18 bold", bg="lightblue", fg="white")
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqt = Label(self.right, text=str(products_quantity[self.counter]), font="arial 18 bold", bg="lightblue", fg="white")
                self.tempqt.place(x=250, y=self.y_index)
                labels_list.append(self.tempqt)

                self.tempprice = Label(self.right, text=str(products_price[self.counter]), font="arial 18 bold", bg="lightblue", fg="white")
                self.tempprice.place(x=500, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index += 40
                self.counter += 1

                self.total_l.configure(text="Total: $ " + str(sum(products_price)))

                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.product.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_button.destroy()


                self.enteride.focus()
                self.enteride.delete(0, END)
    def change_func(self, *args, **kwargs):
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(products_price))

        self.to_give = self.amount_given - self.our_total

        self.c_amount = Label(self.left, text="Change: $ " + str(self.to_give), font="arial 18 bold", fg="red", bg="white")
        self.c_amount.place(x=0, y=600)


    def generate_bills(self, *args, **kwargs):

        directory = "invoice\\" + str(date) + "\\"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Template for the bills

        company = "\t\t\t\tMicheal General Store\n"
        address = "\t\t\t\tLondon, UK\n"
        phone_no = "\t\t\t\t99999999999\n"
        sample = "\t\t\t\tInvoice\n"
        dt = "\t\t\t\t" + str(date)

        table_header = "\n\n\t\t\t----------------------------------------------\n\t\t\tSN.\tProducts\tQty\tAmount\n\t\t\t---------------------------------------------"
        final = company + address + phone_no + sample + dt + "\n" + table_header

        # file to write

        file_name = str(directory) + str(random.randrange(5000, 10000)) + ".txt"
        f = open(file_name, "w")
        f.write(final)

        # file dynamics
        r = 1
        i = 0
        for t in products_list:
            f.write("\n\t\t\t" + str(r) + "\t" + str(products_list[i] + "         ")[:7] + "\t\t" + str(products_quantity[i]) + "\t" + str(products_price[i]))
            i += 1
            r += 1
        f.write("\n\n\t\t\tTotal: $ " + str(sum(products_price)))
        f.write("\n\t\t\tThanks For Visiting")
        os.startfile(file_name, "print")
        f.close()

        self.x = 0
        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (products_id[self.x], ))


        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.get_stock) - int(products_quantity[self.x])
            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, products_id[self.x]))
            conn.commit()

            sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
            c.execute(sql2, (products_list[self.x], products_quantity[self.x], products_price[self.x], date))
            conn.commit()

            self.x += 1

        for a in labels_list:
            a.destroy()

        del(products_list[:])
        del(products_id[:])
        del(products_quantity[:])
        del(products_price[:])
        self.total_l.configure(text="")
        self.c_amount.configure(text="")
        self.change_e.delete(0, END)
        self.enteride.focus()

        tkinter.messagebox.showinfo("Success", "Done everything smoothly")



root =Tk()
b = Application(root)

root.geometry("1530x790+0+0")
root.mainloop()