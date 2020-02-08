from tkinter import *
import workbook as wb



# implements the ability to add stocks into the gui
def add(window, workbook):
    # creates the input boxes for add_stock
    stock_add = Entry(window)
    stock_add.grid(row=0, column=0)
    quantity_add = Entry(window)
    quantity_add.grid(row=0, column=1)

    # gets the strings from the user input
    def add_stock():
        stock = stock_add.get()
        stock_add.delete(0, 'end')
        quantity = quantity_add.get()
        quantity_add.delete(0, 'end')
        wb.add_stock(workbook, stock, quantity)

    # creates the button for add_stock
    add = Button(window, text='Add Stock', command=add_stock)
    add.grid(row=0, column=2, sticky=W)



# implements the ability to delete stocks into the gui
def delete(window, workbook):
    # creates the input box for del_stock
    stock_del = Entry(window)
    stock_del.grid(row=1, column=0)

    # gets the string from the user input
    def del_stock():
        stock = stock_del.get()
        stock_del.delete(0, 'end')
        wb.del_stock(workbook, stock)

    # creates the button for del_stock
    delete = Button(window, text='Delete Stock', command=del_stock)
    delete.grid(row=1, column=2, stick=W)



# implements the ability to change stock quantity into the gui
def change(window, workbook):
    # creates the input boxes for change_stock_q
    stock_change = Entry(window)
    stock_change.grid(row=2, column=0)
    quantity_change = Entry(window)
    quantity_change.grid(row=2, column=1)

    # gets the strings from the user input
    def change_stock_q():
        stock = stock_change.get()
        stock_change.delete(0, 'end')
        quantity = quantity_change.get()
        quantity_change.delete(0, 'end')
        wb.change_stock_q(workbook, stock, quantity)

    # creates the button for change_stock_q
    change = Button(window, text='Change Stock Quantity', command=change_stock_q)
    change.grid(row=2, column=2, sticky=W)



def window(workbook):
    window = Tk()
    window.title(workbook)

    # adds buttons and input into gui
    add(window, workbook)
    delete(window, workbook)
    change(window, workbook)

    window.mainloop()