import yfinance as yf


# returns the open price from the given day as a float
def get_open(stock, date):
    # imports the data from the ticker
    ticker = yf.Ticker(stock)
    ystats = ticker.history(start=date, end=date)
    return float(ystats['Open'][0])


# returns the closing price from the given day as a float
def get_close(stock, date):
    ticker = yf.Ticker(stock)
    ystats = ticker.history(start=date, end=date)
    return float(ystats['Close'][0])


# returns the difference in opening and closing prices for the given date as a float
def get_change(stock, date):
    return get_close(stock, date) - get_open(stock, date)
