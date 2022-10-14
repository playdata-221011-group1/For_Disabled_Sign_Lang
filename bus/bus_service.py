#인증키 fd5e2f7cf46140f2a00f1f27ea890b3c
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import xmltodict
from flask import request


class BusService:
    def trans_list(self):
        url = "https://openapi.gg.go.kr/Ggdspsntaxistus?"
        key = "fd5e2f7cf46140f2a00f1f27ea890b3c"
        type = "json"
        p_index = "1"
        p_size = "200"

        url += "Key=" + key
        url += "&Type=" + type
        url += "&pIndex=" + p_index
        url += "&pSize=" + p_size

        html = requests.get(url).text
        data = json.loads(html)
        #print(data)
        trans = data["Ggdspsntaxistus"][1]["row"] #지원 기관 리스트

        #지원 기관 리스트 DataFrame으로 변환
        trans_pd = pd.DataFrame(trans)
        trans_pd = trans_pd.set_index(["SIGUN_NM"])  #시군명을 index로 지정
        #print(trans_pd)

        return trans

class LowBusService:
    def low_bus_list(self):
        api_key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'
        url = 'http://ws.bus.go.kr/api/rest/stationinfo/getLowStationByName?ServiceKey='
        url += api_key
        html = requests.get(url).text
        html2 = xmltodict.parse(html)
        res1 = json.dumps(html2)
        res2 = json.loads(res1)

        data = res2['ServiceResult']
        data2 = data['msgBody']
        data3 = data2['itemList']
        ################################
        # b_api_key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'
        # b_url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey='
        # b_url += b_api_key
        # b_html = requests.get(b_url).text
        # b_html2 = xmltodict.parse(b_html)
        # b_res1 = json.dumps(b_html2)
        # b_res2 = json.loads(b_res1)
        #
        # b_data = b_res2['ServiceResult']
        # b_data2 = b_data['msgBody']
        # b_data3 = b_data2['itemList'][0]


        return data3

    # def low_bus_list(self):
    #     # 버스이름으로 정보 검색
    #     api_key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'
    #     url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey='
    #     url += api_key
    #     html = requests.get(url).text
    #     html
    #
    #     return html

    def makeUrl(cmd, params):  # 수행하고 싶은 기능에 맞게 url 변경해줌
        url = 'http://ws.bus.go.kr/api/rest/'
        u = url
        u += cmd
        for c in params:
            u += c
        return u

    def getArsIdByStName(self):  # 정거장명을 파람으로 넣으면 arsId 반환
        station = request.args.get('station')
        api_key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'
        cmd = 'stationinfo/getLowStationByName'  # 'stationinfo/getStationByName'
        params = ['?ServiceKey=' + api_key, '&stSrch=' + station] ###
        u = LowBusService.makeUrl(cmd, params)
        html = requests.get(u).text  # url에 요청
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('headerCd').get_text()
        st_arsid = []
        if code == '0':
            items = root.find_all('itemList')  # 배열
            for item in items:
                stNm = item.find('stNm').get_text()
                if station == stNm: ###
                    id = item.find('arsId').get_text()
                    st_arsid.append(id)
        else:
            print('error code:', code)
        return st_arsid

    def getBusListByStArsid(self):
        api_key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'
        cmd = 'stationinfo/getRouteByStation'  # stationinfo/getLowStationByName
        params = ['?ServiceKey=' + api_key, '&arsId=' + LowBusService.getArsIdByStName(self)[0]] ###
        u = LowBusService.makeUrl(cmd, params)
        html = requests.get(u).text  # url에 요청
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('headerCd').get_text()
        bus = []
        if code == '0':
            items = root.find_all('itemList')  # 배열
            for item in items:
                busNm = item.find('busRouteNm').get_text()
                bus.append(busNm)
            return bus
        else:
            print('error code:', code)

    def getBusStopName(self):
        station = request.args.get("station")
        arsid = LowBusService.getArsIdByStName(station) ###
        for a in arsid:
            busList = LowBusService.getBusListByStArsid(a)
            list=[]
            for b in busList:
                list.append(b)
            return list
