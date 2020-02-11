import window as win
import workbook as wb
import os



# sets the name of the workbook and opens the workbook editing window
workbook_title = 'Stocks.xlsx'

# runs window allowing for the user to add delete and change stocks and quantities
win.window(workbook_title)

# fills out any missing dates form the last date entered to the day before runtime
wb.fill_dates(workbook_title)

# opens the workbook with all updates
os.startfile(workbook_title)