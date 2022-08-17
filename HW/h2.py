from bs4 import BeautifulSoup
import urllib.request
#Thanks to Alma for this next line
from datetime import date
import random 
import time 
import csv
import re 

the_link = 'https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks'
the_page = urllib.request.urlopen(the_link)
the_page

soup = BeautifulSoup(the_page.read())
print(soup.prettify())

h3 = soup.find_all('h3')


s