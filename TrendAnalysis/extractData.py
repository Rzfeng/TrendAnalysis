import os
import requests
import re
from bs4 import BeautifulSoup
import search
import pandas as pd

##############################################################################
def parseText(tickers):
    x = []
    with open(tickers) as file:
        for l in file:
            x.append(l.strip())
    return x

def addData(stocks, csvFile):
    with open(csvFile,'a') as fd:
        for x in stocks:
            curLine = str(x) + ',' + curPrice(x) + ',' + netChange(x) + '\n'
            fd.write(curLine)

def getRanks(csvFile):
    f = pd.read_csv(csvFile)
    keep_col = ['Symbol']
    new_f = f[keep_col]
    with open('data.csv','w') as fd:
        rowLabels = 'Symbol,zacks,yahoo,theStreet,investor' + '\n'
        fd.write(rowLabels)
        for index, row in new_f.iterrows():
            curStock = str(row["Symbol"])
            newEntry = ''
            newEntry = curStock + ',' + search.zacks(curStock) + ',' + search.yahoo(curStock) + ',' + search.theStreet(curStock) + ',' + search.investor(curStock) + '\n'
            print(newEntry)
            fd.write(newEntry)

def getResults(csvFile1, csvFile2):
    f1 = pd.read_csv(csvFile1)
    keep_col = ['Symbol', 'Time', 'Estimate', 'Reported', 'Surprise', '%Surp', 'Price Change']
    f1 = f1[keep_col]

    f2 = pd.read_csv(csvFile2)
    f = f1.merge(f2, how='left', on='Symbol')
    print(f.columns.values[8])
    print(f)

    with open('results.csv', 'w') as fd:
            ignore = 1
            epsResult = ''
            priceResult = ''

            colLabels = 'Symbol, eps\%, price%, zacks, yahoo, theStreet, investor' + '\n'
            fd.write(colLabels)
            for index, row in f.iterrows():
                newEntry = str(row["Symbol"]) + ',' + str(row["%Surp"]) + ',' + str(row["Price Change"]) + ',' + str(row["zacks"]) + ',' + str(row["yahoo"]) + ',' + str(row["theStreet"])  + ',' + str(row["investor"]) + '\n'
                print(newEntry)
                fd.write(newEntry)

##############################################################################
getRanks("10:30.csv")

getResults("10:30.csv", "data.csv")
