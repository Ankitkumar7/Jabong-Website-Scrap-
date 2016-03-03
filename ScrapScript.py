'''Jabong Scrap Script'''
#MODULE INCLUDED
from lxml import html
import requests
from lxml import html
import requests
from pprint import pprint
import urllib
import re
from tabulate import tabulate



lines=[25, 29]
i=0
f=open('url.txt')

lines=f.readlines()
i=0
for i in range(len(lines)):
    lines[i]
    i+=1




for i in range(len(lines)):
    url1 = lines[i+2].rstrip('\n')
    i+=1
    page = requests.get(url1)
    tree = html.fromstring(page.text)
       
    htmlfile_img = urllib.urlopen(url1)
    htmltext_img = htmlfile_img.read()
    Brand_one = tree.xpath('//span[@class="brand"]/text()')
    prices_one = tree.xpath('//span[@itemprop="price"]/text()')
    pro_title_one = tree.xpath('//span[@itemprop="name"]/text()')
    print '\nItem',i
    print '-------------------------------------------------------------------------------------------------------------------------------------------------------------'
    print "Prices"
    print tabulate(prices_one)
    print "Brand Name"
    print tabulate(Brand_one)
    print 'Product Title'
    print tabulate([pro_title_one])
    
      
        

        
        
    
for i in range(len(lines)):
    print Data_retrieve_function()
conn.close()
    
