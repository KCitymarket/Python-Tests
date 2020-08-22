import urllib
import json 
import requests
import time
from urllib.request import Request

#Super simple python code that takes our school cafeteria's menu and prints it
#Q&A Q:"Does it work?" A:"shut up"

urlReq = Request("https://www.sodexo.fi/ruokalistat/output/weekly_json/115", headers = {"User-Agent": "Mozilla/5.0"})
data = urllib.request.urlopen(urlReq).read()
dates = json.loads(data)["timeperiod"]

#these take the correct lists and dates or whatever
#sodMa means sodexo maanantai, sodTi means sodexo tiistai and so on
#sodMaV means sodexo maanantai vegan

sodMa = json.loads(data)["mealdates"][0]
sodMa1 = sodMa["courses"]
sodMa2 = sodMa1["1"]
sodMaV = sodMa1["2"]

sodTi = json.loads(data)["mealdates"][1]
sodTi1 = sodTi["courses"]
sodTi2 = sodTi1["1"]
sodTiV = sodTi1["2"]

sodKe = json.loads(data)["mealdates"][2]
sodKe1 = sodKe["courses"]
sodKe2 = sodKe1["1"]
sodKeV = sodKe1["2"]

sodTo = json.loads(data)["mealdates"][3]
sodTo1 = sodTo["courses"]
sodTo2 = sodTo1["1"]
sodToV = sodTo1["2"]

sodPe = json.loads(data)["mealdates"][4]
sodPe1 = sodPe["courses"]
sodPe2 = sodPe1["1"]
sodPeV = sodPe1["2"]

print(dates, "\n")
print(sodMa["date"])
print(sodMa2["title_fi"])
print(sodMaV["title_fi"], "\n")
print(sodTi["date"])
print(sodTi2["title_fi"])
print(sodTiV["title_fi"], "\n")
print(sodKe["date"])
print(sodKe2["title_fi"])
print(sodKeV["title_fi"], "\n")
print(sodTo["date"])
print(sodTo2["title_fi"])
print(sodToV["title_fi"], "\n")
print(sodPe["date"])
print(sodPe2["title_fi"])
print(sodPeV["title_fi"], "\n")

time.sleep(10)
