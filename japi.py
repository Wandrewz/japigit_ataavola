# Project Deliverable 5
# Andrew Taavola
# japi.py
# March 9, 2020

import urllib
import json


def getStockData(symbol):

    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + \
        symbol + "&apikey=88QHIZ00MWMJU3EA"
    connection = urllib.urlopen(url)
    responseString = connection.read().decode()
    return responseString


def main():
    f = open("japi.out", "a")
    sym = raw_input("Please enter a stock symbol: ")
    while sym != "quit":
        data = getStockData(sym)
        print data
        print >> f, data
        stockdict = json.loads(data)
        stockprice = stockdict['Global Quote']['05. price']
        stockprice = stockprice[:-2]
        print "The current price of", sym, "is: $" + stockprice
        print >> f, "The current price of", sym, "is: $" + stockprice
        sym = raw_input("Please enter a stock symbol: ")
    f.close()
    print "Stock Quotes retrieved succesfully!"


if __name__ == "__main__":
    main()
