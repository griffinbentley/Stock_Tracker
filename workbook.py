from openpyxl import Workbook
from openpyxl import load_workbook
import stock_info as si



def get_stocks(workbook):
    wb = load_workbook(workbook)
    ws = wb.active

    stocks = {}
    col = 66
    while ws[chr(col) + '2'].value != None:
        stocks[ws[chr(col) + '2'].value.split()[0]] = float(ws[chr(col) + '2'].value.split()[1])
        col += 1
    return stocks



# adds stock info for the given date and stocks to the table
def add_date(workbook,stocks,stocks_q,date):
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