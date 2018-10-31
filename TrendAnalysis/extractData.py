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
    with open('document.csv','a') as fd:
        for index, row in new_f.iterrows():
            newEntry = ''
            newEntry = row["Symbol"] + ',' + search.zacks(curStock) + ',' + search.yahoo(curStock) + ',' + search.theStreet(curStock) + ',' + search.investor(curStock)
            fd.write(newEntry)

##############################################################################
getRanks("10:31.csv")


# with open('10:31.csv', 'r') as istr:
#     with open('output.csv', 'w') as ostr:
#         ignore = 1
#         epsResult = ''
#         priceResult = ''
#
#         for line in istr:
#             #EPS Analysis
#             if ignore == 1:
#                 ignore = 0
#             else:
#                 expected = float(line.split(',')[2])
#                 actual = float(line.split(',')[3])
#                 epsChange = str(line.split(',')[5])
#                 epsChange = float(epsChange[:-2])
#                 priceChange = str(line.split(',')[6])
#                 priceChange = float(priceChange[:-2])
#
#
#                 if epsChange < 0:
#                     epsResult = 'Missed'
#                 elif epsChange > 0:
#                     epsResult = 'Exceeded'
#                 else:
#                     epsResult = 'Neutral'
#                 print(epsResult)
#
#                 if priceChange < 0:
#                     priceResult = 'Decrease'
#                 elif priceChange > 0:
#                     priceResult = 'Increase'
#                 else:
#                     priceResult = 'Neutral'
#                 print(priceResult)
#
#             #write to csv file
#             curStock = line.split(',')[0]
#             line = line.rstrip('\n') + ',' + search.zacks(curStock) + ',' + search.yahoo(curStock) + ',' + search.theStreet(curStock) + ',' + search.investor(curStock) + ',' + epsResult + ',' + priceResult
#             print(line)
#             print(line, file=ostr)
