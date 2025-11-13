import datetime
import pandas as pd
import yfinance as yf


start_date = datetime.datetime(2025,1,1)
end_date = datetime.datetime(2025, 11, 13)

meta = yf.Ticker("META")

data = meta.history(start=start_date, end=end_date)

data.to_csv("META.csv", index=True)