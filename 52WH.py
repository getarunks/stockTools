import webbrowser
import json
from urllib2 import urlopen
 
a_website = "https://www.google.com"
 
# Open url in a new window of the default browser, if possible
#webbrowser.open_new(a_website)
 
#https://chartink.com/stocks/jetairways.html
#webbrowser.open_new_tab(a_website)
 
#webbrowser.open(a_website, 1) # Equivalent to: webbrowser.open_new(a_website)
#webbrowser.open(a_website, 2) # Equivalent to: webbrowser.open_new_tab(a_website)

#source = urlopen('https://www.nseindia.com/products/dynaContent/equities/equities/json/online52NewHigh.json')
# Open link and save to 52w.json https://www.nseindia.com/products/dynaContent/equities/equities/json/online52NewHigh.json

filename = '52w.json'
with open(filename, 'r') as f:
        data = json.load(f)
#print data

print "==========="

stock_list = []
for n in data['data']:
    stock = n['symbol'].encode("ascii") # to remove u' from stock symbol
    stock_list.append(stock)
    
print "Total Stocks 52W ", len(stock_list)
print stock_list

#stock_list = stock_list[:5]
count = 0
for n in stock_list:
    link = 'https://chartink.com/stocks/'+n+'.html'
    webbrowser.open_new_tab(link)
    count = count + 1
    if count%5 == 0:
        print "Enter for next"
        chara = raw_input()
        print chara
#data = data['data']
#print data
