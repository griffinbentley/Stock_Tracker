from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Font
import stock_info as si



# grabs the names and quantities of stocks stored in the given worksheet and returns it as a dictionary
def get_stocks(workbook):
    wb = load_workbook(workbook)
    ws = wb.active

    stocks = {}
    col = 66
    while ws[chr(col) + '2'].value != None:
        stocks[ws[chr(col) + '2'].value.split()[0]] = float(ws[chr(col) + '2'].value.split()[1])
        col += 1
    return stocks



# adds a column into the worksheet with the given quantity
def add_stock(workbook, stock, quantity):
    wb = load_workbook(workbook)
    ws = wb.active

    # checks to see if the stock is already in the sheet
    col = 66
    while ws[chr(col) + '2'].value != None and ws[chr(col) + '2'].value.split()[0] != stock:
        col += 1
    if ws[chr(col) + '2'].value != None:
        return 0

    ws.insert_cols(2)
    ws['B2'] = stock + ' ' + str(quantity)

    # moves the 'STOCKS' label over to the correct cell
    ws['B1'] = 'STOCKS'
    ws['B1'].font = Font(bold=True)
    ws['C1'] = ''

    wb.save(workbook)
    return 1



# deletes the given stock from the worksheet
def del_stock(workbook, stock):
    wb = load_workbook(workbook)
    ws = wb.active

    # finds the stock or returns 0 if the stock doesn't exist in the sheet
    col = 66
    while ws[chr(col) + '2'].value != None and ws[chr(col) + '2'].value.split()[0] != stock:
        col += 1
    if ws[chr(col) + '2'].value == None:
        return 0

    # moves 'STOCKS' label if needed
    if ws[chr(col) + '1'].value == 'STOCKS':
        ws[chr(col + 1) + '1'] = 'STOCKS'
        ws[chr(col + 1) + '1'].font = Font(bold=True)

    ws.delete_cols(col - 64)

    wb.save(workbook)
    return 1



# changes the quantity of the given stock from the worksheet
def change_stock_q(workbook, stock, quantity):
    wb = load_workbook(workbook)
    ws = wb.active

    # finds the stock or returns 0 if the stock doesn't exist in the sheet
    col = 66
    while ws[chr(col) + '2'].value != None and ws[chr(col) + '2'].value.split()[0] != stock:
        col += 1
    if ws[chr(col) + '2'].value == None:
        return 0

    # resets the quantity to the given one
    ws[chr(col) + '2'] = stock + ' ' + str(quantity)

    wb.save(workbook)
    return 1



# adds stock info for the given date and stocks to the table
def add_date(workbook, stocks, stocks_q, date):
    wb = load_workbook(workbook)
    ws = wb.active

    # find next open cell in col 'A'
    row = 3
    while ws['A' + str(row)].value != None:
        row += 1

    # check to see if date is already entered
    if ws['A' + str(row - 1)].value == date[5:]:
        return 0

    row = str(row)

    # enters the date and the stock info into the table and stores total in final column
    gain_loss = 0
    ws['A' + row] = date[5:]
    for i in range(len(stocks)):
        col = chr(66 + i)
        change = si.get_change(stocks[i],date)
        ws[col + row] = change
        gain_loss += change * stocks_q[stocks[i]]
    ws[chr(66 + i + 1) + row] = gain_loss

    # adds the total value of all stocks into the sheet
    total = 0
    for s in stocks:
        total += si.get_close(s,date) * stocks_q[s]
    ws[chr(66 + i + 2) + row] = total

    wb.save(workbook)
    return 1