import urllib
import json 
import requests
import time
from urllib.request import Request


urlReq = Request("https://www.sodexo.fi/ruokalistat/output/weekly_json/115", headers = {"User-Agent": "Mozilla/5.0"})
data = urllib.request.urlopen(urlReq).read()

sodMa = json.loads(data)["mealdates"][0]
sodMa1 = sodMa["courses"]
sodMa2 = sodMa1["1"]

sodTi = json.loads(data)["mealdates"][1]
sodTi1 = sodTi["courses"]
sodTi2 = sodTi1["1"]

sodKe = json.loads(data)["mealdates"][2]
sodKe1 = sodKe["courses"]
sodKe2 = sodKe1["1"]

sodTo = json.loads(data)["mealdates"][3]
sodTo1 = sodTo["courses"]
sodTo2 = sodTo1["1"]

sodPe = json.loads(data)["mealdates"][4]
sodPe1 = sodPe["courses"]
sodPe2 = sodPe1["1"]

print(sodMa["date"])
print(sodMa2["title_fi"])
print("")
print(sodTi["date"])
print(sodTi2["title_fi"])
print("")
print(sodKe["date"])
print(sodKe2["title_fi"])
print("")
print(sodTo["date"])
print(sodTo2["title_fi"])
print("")
print(sodPe["date"])
print(sodPe2["title_fi"])

time.sleep(10)
