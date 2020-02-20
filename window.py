from tkinter import *
import workbook as wb
from datetime import datetime


# implements the ability to add stocks into the gui
def add(window, workbook, error, stocks, stock_q):
    # creates the input boxes for add_stock
    stock_add = Entry(window)
    stock_add.grid(row=1, column=0, padx=5, pady=5)
    quantity_add = Entry(window)
    quantity_add.grid(row=1, column=1, padx=5, pady=5)
    window.columnconfigure(0, minsize=140)

    # gets the strings from the user input
    def add_stock():
        stock = stock_add.get()
        quantity = quantity_add.get()

        # checks to make sure that quantity is a positive integer
        if not quantity.isdigit():
            error.configure(text='Quantity must be an integer')
            return
        else:
            stock_add.delete(0, 'end')
            quantity_add.delete(0, 'end')

        # checks to make sure that the stock isn't already in the workbook
        if not wb.add_stock(workbook, stock, quantity):
            error.configure(text='That stock already exists')
        else:
            stock_q[stock] = quantity
            stocks.configure(text=stock_q)
            error.configure(text='')

    # creates the button for add_stock
    add_b = Button(window, text='Add New Stock', command=add_stock)
    add_b.grid(row=1, column=2, sticky=W, padx=5, pady=5)


# implements the ability to delete stocks into the gui
def delete(window, workbook, error, stocks, stock_q):
    # creates the input box for del_stock
    stock_del = Entry(window)
    stock_del.grid(row=2, column=0, padx=5, pady=5)

    # gets the string from the user input
    def del_stock():
        stock = stock_del.get()
        stock_del.delete(0, 'end')

        # checks to make sure the stock is in the workbook
        if not wb.del_stock(workbook, stock):
            error.configure(text='That stock does not exist')
        else:
            stock_q.pop(stock)
            stocks.configure(text=stock_q)
            error.configure(text='')

    # creates the button for del_stock
    delete_b = Button(window, text='Delete Stock', command=del_stock)
    delete_b.grid(row=2, column=2, stick=W, padx=5, pady=5)


# implements the ability to change stock quantity into the gui
def change(window, workbook, error, stocks, stock_q):
    # creates the input boxes for change_stock_q
    stock_change = Entry(window)
    quantity_change = Entry(window)
    stock_change.grid(row=3, column=0, padx=5, pady=5)
    quantity_change.grid(row=3, column=1, padx=5, pady=5)

    # gets the strings from the user input
    def change_stock_q():
        stock = stock_change.get()
        quantity = quantity_change.get()

        # checks to make sure that quantity is a positive integer
        if not quantity.isdigit():
            error.configure(text='Quantity must be an integer')
            return
        else:
            stock_change.delete(0, 'end')
            quantity_change.delete(0, 'end')

        # checks to make sure the stock is in the workbook
        if not wb.change_stock_q(workbook, stock, quantity):
            error.configure(text='That stock does not exist')
        else:
            stock_q[stock] = quantity
            stocks.configure(text=stock_q)
            error.configure(text='')

    # creates the button for change_stock_q
    change_b = Button(window, text='Change Stock Quantity', command=change_stock_q)
    change_b.grid(row=3, column=2, sticky=W, padx=5, pady=5)


# opens window to get the start date from the user and returns it
def init_date_win(workbook, stocks, stocks_q):
    window = Tk()
    window.title('Pick Start Date')
    window.configure(bg='light grey')

    # creates entry box and error label
    date_e = Entry(window)
    date_e.grid(row=0, column=0, padx=5, pady=5)
    error = Label(window, fg='red', bg='light grey')
    error.grid(row=1, column=0)

    # gets the date from the entry box and checks if it's a valid date
    def get_date():
        date_str = date_e.get()

        # if format is right and date isn't a weekend, return the date and close the window
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if date.weekday() == 5 or date.weekday() == 6:
                error.configure(text='Stock market not open on weekends')
            else:
                wb.add_date(workbook, stocks, stocks_q, date)
                window.destroy()

        # if ValueError then tell user that the date is in the wrong format
        except ValueError:
            error.configure(text='Date in wrong format')

        # if IndexError then tell the user that the date entered is a holiday
        except IndexError:
            error.configure(text='Date is holiday')

    date_b = Button(window, text='Enter Start Date (Y-M-D)', command=get_date)
    date_b.grid(row=0, column=1, sticky=W, padx=5, pady=5)

    window.mainloop()


# main loop to get buttons and input setup
def main_window(workbook):
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
