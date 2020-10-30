from yahoo_finance_api2 import share
from datetime import datetime
import pandas as pd
df = pd.read_csv("teslaDataset.csv")

stock = share.Share("TSLA")
weekData = dict(stock.get_historical(share.PERIOD_TYPE_DAY,6,share.FREQUENCY_TYPE_DAY,1))

for x in range(len(weekData["timestamp"])):
	timestamp = int(str(int(int((weekData["timestamp"][x]))/1000)))
	dt_object = datetime.fromtimestamp(timestamp)
	dt_object = str(dt_object)
	dt_object = dt_object[:10]
	someDict = weekData
	weekData["timestamp"][x] = dt_object
	weekData = dict(weekData)
# print(weekData)
# input a dictionary with keys with "low" and "timestamp"
def findSlope(someList):
	slopeList = []
	for x in range(len(someList["low"])-1):
		day1 = someList["low"][x]
		day2 = someList["low"][x + 1]
		slopeList.append(round(day2 - day1,2))
	for w in range(len(someList["timestamp"])):
		slopeList.append(someList["timestamp"][w])
	return slopeList
def findratios(listOfSlope):
	lenOflistOfSlope = len(listOfSlope)
	listOfRatios = []
	validindexes = int(lenOflistOfSlope/2 - 0.5)
	for q in range(validindexes-1):
		listOfRatios.append(round((listOfSlope[q+1]/listOfSlope[q]),3))
	return listOfRatios
# print(findSlope(weekData))

