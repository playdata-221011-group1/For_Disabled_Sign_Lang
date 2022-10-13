#인증키 fd5e2f7cf46140f2a00f1f27ea890b3c
import requests
import json
import pandas as pd

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
        print(trans_pd)

        return trans
