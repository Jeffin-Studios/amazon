import os
import sys
import ntpath
import glob
import shutil

from urllib.parse import urlparse
from requests_html import HTMLSession

from lxml import html  
import csv,os,json
import requests
from time import sleep

session = HTMLSession()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}


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
	url="https://www.amazon.com/dp/"+ASIN 
	response = session.get(url, headers=headers, verify=False) 
	print(response.html.search('a-color-price">${}<')[0]) #Extracting the price


def AmzonParser(url):

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(url,headers=headers)
	while True:
		sleep(3)
		doc = html.fromstring(page.content)
		XPATH_NAME = '//h1[@id="title"]//text()'
		XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
		XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
		XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
		XPATH_AVAILABILITY = '//div[@id="availability"]//text()'

		RAW_NAME = doc.xpath(XPATH_NAME)
		RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
		RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
		RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
		RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)

		NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
		SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
		CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
		ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
		AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None

		if not ORIGINAL_PRICE:
			ORIGINAL_PRICE = SALE_PRICE

		data = {
				'NAME':NAME,
				'SALE_PRICE':SALE_PRICE,
				'CATEGORY':CATEGORY,
				'ORIGINAL_PRICE':ORIGINAL_PRICE,
				'AVAILABILITY':AVAILABILITY,
				'URL':url,
				}

		return data

def extract(ASIN):
	extracted_data = []
	url = "http://www.amazon.com/dp/"+ASIN
	print ("Processing: "+url)
	extracted_data.append(AmzonParser(url))
	sleep(5)
	data_file=open('data.json','w')
	json.dump(extracted_data,data_file,indent=4)	



if __name__ == '__main__':
	(product_name, ASIN) = getInfo("https://www.amazon.com/MAGTIMES-Rainbow-Anti-Anxiety-Spinner-Relieving/dp/B072LNQBZT/ref=sr_1_5?s=toys-and-games&ie=UTF8&qid=1537316629&sr=1-5&keywords=fidget%20spinner")
	retrieve(ASIN)
	extract(ASIN)







