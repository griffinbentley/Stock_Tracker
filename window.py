from tkinter import *
import workbook as wb



# implements the ability to add stocks into the gui
def add(window, workbook, error, stocks, stock_q):
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
        if not wb.add_stock(workbook, stock, quantity):
            error.configure(text='That stock already exists')
        else:
            stock_q[stock] = quantity
            stocks.configure(text=stock_q)
            error.configure(text='')

    # creates the button for add_stock
    add = Button(window, text='Add New Stock', command=add_stock)
    add.grid(row=1, column=2, sticky=W, padx=5, pady=5)



# implements the ability to delete stocks into the gui
def delete(window, workbook, error, stocks, stock_q):
    # creates the input box for del_stock
    stock_del = Entry(window)
    stock_del.grid(row=2, column=0, padx=5, pady=5)

    # gets the string from the user input
    def del_stock():
        stock = stock_del.get()
        stock_del.delete(0, 'end')
        if not wb.del_stock(workbook, stock):
            error.configure(text='That stock does not exist')
        else:
            stock_q.pop(stock)
            stocks.configure(text=stock_q)
            error.configure(text='')

    # creates the button for del_stock
    delete = Button(window, text='Delete Stock', command=del_stock)
    delete.grid(row=2, column=2, stick=W, padx=5, pady=5)



# implements the ability to change stock quantity into the gui
def change(window, workbook, error, stocks, stock_q):
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
        if not wb.change_stock_q(workbook, stock, quantity):
            error.configure(text='That stock does not exist')
        else:
            stock_q[stock] = quantity
            stocks.configure(text=stock_q)
            error.configure(text='')

    # creates the button for change_stock_q
    change = Button(window, text='Change Stock Quantity', command=change_stock_q)
    change.grid(row=3, column=2, sticky=W, padx=5, pady=5)



# main loop to get buttons and input setup
def window(workbook):
    window = Tk()
    window.title(workbook)
    window.configure(bg='light grey')

    # creates a frame to put buttons and inputs in
    frame = Frame(window)
    frame.configure(bg='light grey')
    frame.pack()

    # labels for text input boxes
    sl = Label(frame, text='Stock:', font='bold', bg='light grey')
    sl.grid(row=0, column=0, sticky=W, padx=5)
    ql = Label(frame, text='Quantity:', font='bold', bg='light grey')
    ql.grid(row=0, column=1, sticky=W, padx=5)
    error = Label(frame, text='', fg='red', bg='light grey')
    error.grid(row=4, column=0)

    # displays stocks currently stored in the workbook
    stock_q = wb.get_stocks(workbook)
    stocks = Label(window, text=stock_q, bg='light grey')
    stocks.pack()

    # adds buttons and input into gui
    add(frame, workbook, error, stocks, stock_q)
    delete(frame, workbook, error, stocks, stock_q)
    change(frame, workbook, error, stocks, stock_q)

    window.mainloop()