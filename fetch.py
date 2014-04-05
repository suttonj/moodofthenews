#!/usr/bin/env python

import sys
import json
import base64
import urllib2
import urllib
import requests
from bs4 import BeautifulSoup

def fetch_news:
	#Google News
	url = "https://news.google.com/"
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
	articles = soup.find_all(".section-content .esc-lead-article-title")

	data = {}
	for a in articles:
		title = a.string.strip()
	    data[title] = a.attrs['href']
