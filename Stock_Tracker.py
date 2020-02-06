import workbook as wb
import window as win
from datetime import datetime,timedelta


win.window()


workbook_title = 'Stocks.xlsx'

stocks_q = wb.get_stocks(workbook_title)
stocks = list(stocks_q.keys())

yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

if wb.add_date(workbook_title, stocks, stocks_q, yesterday):
    print('Sheet update successful')
else:
    print('Sheet update unsuccessful: date already entered')