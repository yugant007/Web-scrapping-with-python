import requests

from bs4 import BeautifulSoup

import csv

page=requests.get("https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card")

soup=BeautifulSoup(page.content,"html.parser")

graphics_cards=soup.select(".item-container")

csv_file=open("D:\py\scrapnewegg\graph.csv",'w')

write=csv.writer(csv_file)

header=["brand","title","rating","price","shipping_rate"]

write.writerow(header)

for container in graphics_cards:

  if (container.select("div div .item-rating")) == []:
    
    rating="No Rating"
    
  else:
    
    rating=(container.select("div div .item-rating"))[0]["title"]
  
  price="$"+(container.select("div div ul .price-current strong"))[0].get_text()
  
  title=(container.select("div .item-title"))[0].get_text()
  
  if container.select("div div a img") == []:
    
    brand=title[0:8]
    
  else:
    
    brand=(container.select("div div a img"))[0]["title"]
    
  if (container.select("div div ul .price-ship"))[0].get_text().strip() == "":
    
    shipping_rate="00"
    
  else:
    
    shipping_rate=(container.select("div div ul .price-ship"))[0].get_text()
    
  write.writerow([brand,title.replace(","," "),rating,price.replace(",",""),shipping_rate,"ll"])

