import requests
from bs4 import BeautifulSoup
import pandas as pd

#bringing URL from required page
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XmxvLc4zbIU")
 #to bring that page content we use beautiful soup
soup = BeautifulSoup(page.content, "html.parser")

week = soup.find(id="seven-day-forecast-body")
# sample
# week= soup.find(id= "current-conditions-body")
#print(week)

items = week.find_all(class_= "tombstone-container")
#print(items)
#print(items[0])
period_names=[]
short_descriptions=[]
temperatures=[]
for i in range(len(items)):
    #items[i].find(class_="period-name").get_text()
    period_names.append(items[i].find(class_="period-name").get_text())
    #items[i].find(class_="short-desc").get_text()
    short_descriptions.append(items[i].find(class_="short-desc").get_text())
    #items[i].find(class_="temp").get_text()
    temperatures.append(items[i].find(class_="temp").get_text())
#print(period_names)
#print(short_descriptions)
#print(temperatures)

#prints the regular text lists into tables
weather_stuff=pd.DataFrame({
    "period":period_names,
    "short_descriptions":short_descriptions,
    "temperatures":temperatures
})
print(weather_stuff)

#to download as CSV file

weather_stuff.to_csv("weather.csv")
