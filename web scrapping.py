from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

# request server to get access
path = requests.get("https://weather.com/en-IN/weather/tenday/l/Lucknow+Uttar+Pradesh?canonicalCityId=aed375757b862f3d6b0826a5ad040d907088036838c0926799b388ec3d15772c")

# reading content from web page
soup = BeautifulSoup(path.content, 'html.parser')

data_set_of_day = soup.find_all(class_ = "DetailsSummary--DetailsSummary--2HluQ DetailsSummary--fadeOnOpen--vFCc_")

# getting day in a list
day =  [item.find(class_="DetailsSummary--daypartName--2FBp2").get_text() for item in data_set_of_day]
print(day)

# getting temperature lows/highs
highs = [item.find(class_ = 'DetailsSummary--highTempValue--3Oteu').get_text() for item in data_set_of_day]
lows = [item.find(class_ = 'DetailsSummary--lowTempValue--3H-7I').get_text() for item in data_set_of_day]
temperatures = [highs,lows]
print(temperatures)

# getting summary condition
#condition = [item.find_all('title') for item in data_set_of_day] ----alternate method (jugaad)
fetching_con = [item.find(class_ = 'DetailsSummary--condition--24gQw') for item in data_set_of_day]
con = [item.find('title').get_text() for item in fetching_con]
print(con)

# getting precipitation
fetching_class = [item.find(class_ = 'DetailsSummary--precip--1ecIJ') for item in data_set_of_day]
perci = [item.find('span').get_text() for item in fetching_class]
print(perci)

weather_report = pd.DataFrame({"Day":day,
                               "High Temperature":highs,
                               "Low Temperature":lows,
                               "Condition":con,
                               "Percipitation":perci})
print(weather_report)

weather_report.to_csv("weather report.csv")