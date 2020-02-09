from tkinter import *
import workbook as wb



# implements the ability to add stocks into the gui
def add(window, workbook):
    # creates the input boxes for add_stock
    stock_add = Entry(window)
    stock_add.grid(row=1, column=0, padx=5, pady=5)
    quantity_add = Entry(window)
    quantity_add.grid(row=1, column=1,padx=5,pady=5)
    window.columnconfigure(0, minsize=140)

    # gets the strings from the user input
    def add_stock():
        stock = stock_add.get()
        stock_add.delete(0, 'end')
        quantity = quantity_add.get()
        quantity_add.delete(0, 'end')
        error(window, wb.add_stock(workbook, stock, quantity), 'That stock already exists')

    # creates the button for add_stock
    add = Button(window, text='Add New Stock', command=add_stock)
    add.grid(row=1, column=2, sticky=W, padx=5, pady=5)



# implements the ability to delete stocks into the gui
def delete(window, workbook):
    # creates the input box for del_stock
    stock_del = Entry(window)
    stock_del.grid(row=2, column=0, padx=5, pady=5)

    # gets the string from the user input
    def del_stock():
        stock = stock_del.get()
        stock_del.delete(0, 'end')
        error(window, wb.del_stock(workbook, stock), 'That stock does not exist')

    # creates the button for del_stock
    delete = Button(window, text='Delete Stock', command=del_stock)
    delete.grid(row=2, column=2, stick=W, padx=5, pady=5)



# implements the ability to change stock quantity into the gui
def change(window, workbook):
    # creates the input boxes for change_stock_q
    stock_change = Entry(window)
    stock_change.grid(row=3, column=0, padx=5, pady=5)
    quantity_change = Entry(window)
    quantity_change.grid(row=3, column=1, padx=5, pady=5)

    # gets the strings from the user input
    def change_stock_q():
        stock = stock_change.get()
        stock_change.delete(0, 'end')
        quantity = quantity_change.get()
        quantity_change.delete(0, 'end')
        error(window, wb.change_stock_q(workbook, stock, quantity), 'That stock does not exist')

    # creates the button for change_stock_q
    change = Button(window, text='Change Stock Quantity', command=change_stock_q)
    change.grid(row=3, column=2, sticky=W, padx=5, pady=5)



# displays the error message given if a failure was detected, or clears the cell if there was a success
def error(window, success, message):
    if success:
        error = Label(window, text='                                          ', bg='light grey')
    else:
        error = Label(window, text=message, fg='red', bg='light grey')
    error.grid(row=4, column=0)


# main loop to get buttons and input setup
def window(workbook):
    window = Tk()
    window.title(workbook)
    window.configure(bg='light grey')
    frame = Frame(window)

    # labels for text input boxes
    sl = Label(window, text='Stock:', font='bold', bg='light grey')
    sl.grid(row=0, column=0, sticky=W, padx=5)
    ql = Label(window, text='Quantity:', font='bold', bg='light grey')
    ql.grid(row=0, column=1, sticky=W, padx=5)
    error(window, 1, '')


    # adds buttons and input into gui
    add(window, workbook)
    delete(window, workbook)
    change(window, workbook)

    window.mainloop()