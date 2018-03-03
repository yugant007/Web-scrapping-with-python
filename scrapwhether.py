import pandas as pd

import requests

from bs4 import BeautifulSoup

'''
Just go to https://www.weather.gov/
Search your city name and enter into the form field
After that you will be taken to your city weather forcast
Copy the link and paste it into below get field
Run the script and see your city weekly weather
'''
page=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WprSqqiWbIU")

soup=BeautifulSoup(page.content,"html.parser")

seven_day=soup.find(id="seven-day-forecast")

period_tags=seven_day.select(".tombstone-container .period-name")

periods=[pt.get_text() for pt in period_tags]

short_descs=[sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

temps=[t.get_text() for t in seven_day.select(".tombstone-container .temp")]

descs=[d["title"] for d in seven_day.select(".tombstone-container img")]

whether=pd.DataFrame({
    
      "period":periods,
      
      "short_desc":short_descs,
      
      "temp":temps,
      
      "desc":descs
      
    })

print(whether)
