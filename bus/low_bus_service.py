import requests
import xmltodict
from bs4 import BeautifulSoup
from flask import json
# getBusRouteList?ServiceKey='

class LowBusService:
    def low_bus_list(self):
        api_key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'
        url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey='
        url += api_key
        html = requests.get(url).text
        html2 = xmltodict.parse(html)
        res1 = json.dumps(html2)
        res2 = json.loads(res1)


        # print(html)
   #     ll = html["edStationNm"]




        return res1