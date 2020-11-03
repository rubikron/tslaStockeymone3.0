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
weekPercents = [[0.010469196510098401, '2010-11-04', '2010-11-05'], [-0.043938975190562404, '2010-11-05', '2010-11-08'], [0.011846701366300918, '2010-11-08', '2010-11-09'], [-0.0554730150481237, '2010-11-09', '2010-11-10']]


def findPercentChanges(df,category):
	lenOflistOfSlope = len(df[category])
	listOfPercents = []
	for r in range(lenOflistOfSlope-1):
		listOfPercents.append([(df[category][r+1] - df[category][r])/df[category][r],tsladf['timestamp'][r],tsladf['timestamp'][r+1]])
	return listOfPercents

listOfDataPercentsClose = findPercentChanges(tsladf,'close')
percentDifs = []
for i in range(len(listOfDataPercentsClose)-2):
	p1 = listOfDataPercentsClose[i][0]
	p2 = listOfDataPercentsClose[i+1][0]
	p3 = listOfDataPercentsClose[i+2][0]
	
	percentDifs.append([abs(weekPercents[0][0]-p1),abs(weekPercents[1][0]-p2),abs(weekPercents[2][0]-p3),listOfDataPercentsClose[i][1],listOfDataPercentsClose[i+2][2]])


avgPercent = []
for d in percentDifs:
	avgPercent.append([(d[0] + d[1] + d[2])/3,d[-2],d[-1]])


avgPercentFirst = []
for e in range(len(avgPercent)):
	avgPercentFirst.append(float(avgPercent[e][0]))
	
someList = avgPercentFirst
avgPercentFirst.sort()
 

recentDates = []
for x in avgPercent:
	for t in range(7):

		if avgPercentFirst[t] == x[0]:
			recentDates.append(int(x[1][0:4]))
			if int(x[1][0:4]) <= recentDates[-1]:
				recentDates.pop(-1)
				recentDates.append(x)
recentDates.pop(0)
priceDict = dict()
priceDict["startPrice"] = 388.04
priceDict["startDate"] = "2020-10-29"

for i in recentDates:
	startDate = i[2]
	indexStartDate = list(tsladf['timestamp']).index(startDate)
	priceDict[tsladf['timestamp'][indexStartDate]] = [tsladf["close"][indexStartDate],indexStartDate]
	priceDict[tsladf['timestamp'][indexStartDate+1]] = [tsladf["close"][indexStartDate+1],indexStartDate + 1]
	priceDict[tsladf['timestamp'][indexStartDate+2]] = [tsladf["close"][indexStartDate+2],indexStartDate + 2]



