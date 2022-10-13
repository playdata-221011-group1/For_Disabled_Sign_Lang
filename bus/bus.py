import json

import requests
import xmltodict
from bs4 import BeautifulSoup


# Service
class BusService:

    # 버스 인덱스 화면에서 수어 리스트 뿌려주는 함수
    def get_all(self):
        url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey=%2FUSr%2Fec%2F4ywJMNg1N9o%2B2cn%2FWo0MfbowBcc5vnFaY0S9jl3UlGVoJaASiHDTTEu%2Fdyb5iN%2BcHMIBOnYfdgb34A%3D%3D'
        #url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=lngSweqj5VjrFqcUQWLMyvM6OKEME1J3'
        ### xml 시도 ###
        # html = requests.get(url).text  # url에 요청
        # print(html)
        # root = BeautifulSoup(html, 'lxml-xml')

        ### json 시도 ###
        html1 = requests.get(url).text
        html2 = xmltodict.parse(html1)
        res1 = json.dumps(html2)
        res2 = json.loads(res1)
        print(res2)
        return res2


    def get_by_bus(self):
        pass
