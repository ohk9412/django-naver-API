from django.test import TestCase
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen
import urllib


a =


query= urllib.parse.quote(a)

target_site = f'https://search.shopping.naver.com/search/all?query={query}&pagingIndex=1&pagingSize=40&productSet=total'
url = target_site
res = urlopen(url)

soup = BeautifulSoup(res, 'html5lib')

for td in soup.select('.basicList_title__3P9Q7'): 
      
    print(td.a.string.strip()) 