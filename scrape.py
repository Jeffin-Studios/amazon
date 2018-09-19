import os
import sys
import ntpath
import glob
import shutil
import csv
from urllib.parse import urlparse
from requests_html import HTMLSession

session = HTMLSession()

def parse(s, first, last):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

def getInfo(url):
	url_info = urlparse(url)
	if (url_info[1] == "www.amazon.com"):
		product_name = parse(url_info[2], '/', '/')
		ASIN = parse(url_info[2], 'dp/', '/')
		print(product_name)
		print(ASIN)
		return (product_name, ASIN)
	return null
	# should store these urls in a csv for future use

def retrieve(ASIN):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	url="https://www.amazon.com/dp/"+ASIN 
	response = session.get(url, headers=headers, verify=False) 
	print(response)
	# response.html.search('a-color-price">${}<')[0]) #Extracting the price

if __name__ == '__main__':
	(product_name, ASIN) = getInfo("https://www.amazon.com/MAGTIMES-Rainbow-Anti-Anxiety-Spinner-Relieving/dp/B072LNQBZT/ref=sr_1_5?s=toys-and-games&ie=UTF8&qid=1537316629&sr=1-5&keywords=fidget%20spinner")
	retrieve(ASIN)






