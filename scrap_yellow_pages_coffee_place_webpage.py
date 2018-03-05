import requests

from bs4 import BeautifulSoup

import csv

csv_file=open("D:\py\scrapyellow\data.csv","w")

write=csv.writer(csv_file)

header=["shop_name","address","phone_number"]

write.writerow(header)

url="https://www.yellowpages.com/search?search_terms=coffee+shops&geo_location_terms=Los+Angeles%2C+CA"

for i in range (1,31):
    
  u=""
  if i!=1:
      
      u=url+"&page="+str(i)
      
  else:
      
      u=url

  query=requests.get(u)

  soup=BeautifulSoup(query.content,"html.parser")

  coffee_shop=soup.select(".result")

  row=[]
  for shop in coffee_shop:

    row=[]
    
    if shop.select(".info h2 a span")!=[]:

       shop_name=shop.select(".info h2 a span")[0].get_text()

       row.append(shop_name)

    if shop.select(".info .info-section .adr")!=[]:
        
        address=shop.select(".info .info-section .adr")[0].get_text().replace(",","")

        row.append(address)
        
    if shop.select(".phone")!=[]:
        
        phone_number=shop.select(".phone")[0].get_text()

        row.append(phone_number)

    if row!=[]:

        write.writerow(row)
