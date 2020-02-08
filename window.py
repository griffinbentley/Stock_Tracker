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



    window.mainloop()