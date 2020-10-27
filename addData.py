from yahoo_finance_api2 import share
from datetime import datetime
import pandas as pd

stock = share.Share("TSLA")
totalHist = dict(stock.get_historical(share.PERIOD_TYPE_YEAR,10,share.FREQUENCY_TYPE_DAY,1))
# print(totalHist)
dfToAppend = pd.DataFrame(totalHist)
dfToAppend.to_csv("teslaDataset.csv")