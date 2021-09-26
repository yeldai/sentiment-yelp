import requests

from bs4 import BeautifulSoup

r= requests.get("https://www.yelp.com/biz/dumpling-baby-china-bistro-san-francisco-4")

soup = BeautifulSoup(r.text,'html.parser')

divs = soup.findAll(class_="review__373c0__3MsBX")
review=[]

for div in divs:
    print(div.find('p').text,'\n')