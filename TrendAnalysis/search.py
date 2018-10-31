import os
import requests
#re helps with string splitting
import re
from bs4 import BeautifulSoup

def curPrice(stock):
    url = 'https://www.zacks.com/stock/quote/' + str(stock).lower()
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
    soup = BeautifulSoup(r.content, "html.parser")
    search = soup.find_all("div", {"id": "get_last_price"})
    count = 0
    str(search)
    search = str(search[0])
    search = re.sub('<[^>]+>', '', search)

    return str(search)

def netChange(stock):
    url = 'https://www.zacks.com/stock/quote/' + str(stock).lower()
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
    soup = BeautifulSoup(r.content, "html.parser")
    search = soup.find_all("div", {"class": "change"})
    count = 0
    str(search)
    search = str(search[0])
    search = re.sub('<[^>]+>', '', search)
    result = ''
    for x in search.split():
        result = result + x + ' '

    return str(result)


def zacks(stock):
    url = 'https://www.zacks.com/stock/quote/' + str(stock).lower()
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
    soup = BeautifulSoup(r.content, "html.parser")
    search = soup.find_all("p", {"class": "rank_view"})
    count = 0
    str(search)
    if search == None or len(search) == 0:
        return "None"
    search = search[0]
    result = ''

    for item in search:
        count += 1
        result = str(item)
        break

    result = result.lstrip()

    return result

def yahoo(stock):
	#url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
	url = 'https://finance.yahoo.com/quote/' + stock.upper() + '?p=' + stock.upper() + '&.tsrc=fin-srch'
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	soupStr = str(soup)
	str1 = "recommendationKey"
	spot = soupStr.find(str1)
	ans = soupStr[spot+20:spot+22]
	if ans == 'bu':
		ans2 = "BUY"
	elif ans == 'st':
		ans2 = "STRONG BUY"
	elif ans == 'ho':
		ans2 = "HOLD"
	elif ans == 'un':
		ans2 = "SELL"
	elif ans == 'se':
		ans2 = "STRONG SELL"
	else:
		ans2 = 'None'

	return str(ans2)

def theStreet(stock):
    url = 'https://www.thestreet.com/quote/' + str(stock).lower() + '.html'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
    soup = BeautifulSoup(r.content, "html.parser")
    search = soup.find_all("div", {"class": "quote-nav-rating-qr-label-container"})
    count = 0
    str(search)
    if search == None or len(search) == 0:
        return "None"
    search = str(search[0])
    search = re.sub('<[^>]+>', '', search)
    try:
        search.split()[4]
        search.split()[3]
    except IndexError:
        return "None"
    result = search.split()[3] + ' ' + search.split()[4]

    return (result)

def investor(stock):
    url = 'https://investorplace.com/stock-quotes/' + stock.lower() + '-stock-quote/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    search = soup.find_all("div", {"id":"stock_analysis_ctrl_box"})

    for item in search:
        step1=item.find_all("h4", {"class": "grade"})
        l = step1[1].text

    return str(l)
