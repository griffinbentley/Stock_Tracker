from tkinter import *
import workbook as wb

def window(workbook):
    window = Tk()
    window.title('Stock Tracker')

    # implements the ability to add stocks into the gui
    # creates the input boxes for add_stock
    stock_add = Entry(window)
    stock_add.grid(row=0, column=0)
    quantity_add = Entry(window)
    quantity_add.grid(row=0,column=1)
    # gets the strings from the user input
    def add_stock():
        stock = stock_add.get()
        quantity = quantity_add.get()
        wb.add_stock(workbook, stock, quantity)
    # creates the button for add_stock
    add = Button(window, text='Add Stock', command=add_stock)
    add.grid(row=0, column=2, sticky=W)

    # implements the ability to delete stocks into the gui
    # creates the input box for del_stock
    stock_del = Entry(window)
    stock_del.grid(row=1, column=0)
    # gets the string from the user input
    def del_stock():
        stock = stock_del.get()
        wb.del_stock(workbook, stock)
    # creates the button for del_stock
    delete = Button(window, text='Delete Stock', command=del_stock)
    delete.grid(row=1, column=2, stick=W)


    window.mainloop()