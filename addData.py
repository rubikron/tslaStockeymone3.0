from yahoo_finance_api2 import share
from datetime import datetime
import pandas as pd


stock = share.Share("TSLA")
totalHist = dict(stock.get_historical(share.PERIOD_TYPE_YEAR,10,share.FREQUENCY_TYPE_DAY,1))
# print(totalHist)


for x in range(len(totalHist["timestamp"])):
	timestamp = int(str(int(int((totalHist["timestamp"][x]))/1000)))
	dt_object = datetime.fromtimestamp(timestamp)
	dt_object = str(dt_object)
	dt_object = dt_object[:10]
	someDict = totalHist
	totalHist["timestamp"][x] = dt_object
	totalHist = dict(totalHist)
dfToAppend = pd.DataFrame(totalHist)
dfToAppend.to_csv("teslaDataset.csv")