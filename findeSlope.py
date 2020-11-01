from yahoo_finance_api2 import share
from datetime import datetime
import pandas as pd

tsladf = pd.read_csv("teslaDataset.csv")
tsladf = tsladf.drop(["unnamed"], axis = 1)

#-------------------------------------------------------------------
# Note: After iteration segment, copy paste the code from the untitled file to the right of this one between these two dashed lines
#-------------------------------------------------------------------

# iterating through teslaDataset and comparing slope ratios with current ones
#for testing purposes
weekRatios = [-1.396, -0.033, -59.457]
# input a dictionary with keys with "low" and "timestamp"
def findSlope(someList,category):
	slopeList = []
	for x in range(len(someList[category])-1):
		day1 = someList[category][x]
		day2 = someList[category][x + 1]
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


# listOfDataRatiosLow = findratios(findSlope(tsladf,'low'))
# listOfDataRatiosHigh = findratios(findSlope(tsladf,'high'))
# listOfDataRatiosOpen = findratios(findSlope(tsladf,'open'))
listOfDataRatiosClose = findSlope(tsladf,'close')	
print(listOfDataRatiosClose)


# ratioDifList = []
# for t in range(len(listOfDataRatiosClose-3)):
# 	closePr1 = listOfDataRatiosClose[t]
# 	closePr2 = listOfDataRatiosClose[t+1]
# 	closePr3 = listOfDataRatiosClose[t+2]
# 	ratioDifList.append()
	
	
	