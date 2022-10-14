import json
import requests

class LiftService:
    def __init__(self):
        url = 'http://openapi.seoul.go.kr:8088/494b534f5664656c313031797253524c/json/SeoulMetroFaciInfo/1/300/'
        json_data = requests.get(url).text
        data = json.loads(json_data)
        self.data = data['SeoulMetroFaciInfo']["row"]
        for a in self.data:
            a['STATION_NM']=a['STATION_NM'].strip('(1)')
            a['STATION_NM']=a['STATION_NM'].strip('(2)')
            a['FACI_NM']=a['FACI_NM'].lstrip('승강기)')


    def station(self):
        stationNm = []
        for s in self.data:
            if s['STATION_NM'] not in stationNm:
                stationNm.append(s['STATION_NM'])
        print(stationNm)
        return stationNm

    def count(self):
        counts = {}

        for i in self.data:
            if i["STATION_NM"] not in counts.keys():
                counts.setdefault(i['STATION_NM'], 1)
            else:
                counts[i['STATION_NM']] += 1
        key, value = list(counts.keys()), list(counts.values())
        return key, value

    def stationInfo(self, station):
        liftInfo = []
        for i in self.data:
            if station in i['STATION_NM']:
                liftInfo.append(i)
        return liftInfo



