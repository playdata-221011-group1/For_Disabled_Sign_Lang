#인증키 fd5e2f7cf46140f2a00f1f27ea890b3c
import requests
import json

class BusService:
    def bus_list(self):
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
        print(data)
        bus_list = data["Ggdspsntaxistus"][1]["row"]

        return bus_list
