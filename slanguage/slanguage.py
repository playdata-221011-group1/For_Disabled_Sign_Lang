import  requests, json
import xmltodict
from flask import request



# Service
class SLanguageService:
    pass
    # # 인덱스 화면에서 수어 리스트 뿌려주는 함수
    # def get_all(self):
    #
    #     url = 'http://api.kcisa.kr/API_CNV_054/request?serviceKey=ecfd5295-71b0-422f-8cd7-7c3cadc4b498'
    #     html = requests.get(url).text  # 웹요청
    #     html2 = xmltodict.parse(html)
    #     res1 = json.dumps(html2)
    #     res2 = json.loads(res1)
    #
    #     data1 = res2['response']
    #     data2 = data1['body']
    #     data3 = data2['items']
    #     data4 = data3['item']
    #     return data4
    #
    # # 수어 클릭하면 title을 파라미터로 보내서 수어 상세내용 출력해주는 함수
    # def get_by_title(self):
    #     title = request.args.get('title')
    #
    #     url = 'http://api.kcisa.kr/API_CNV_054/request?serviceKey=ecfd5295-71b0-422f-8cd7-7c3cadc4b498'
    #
    #     html = requests.get(url).text  # 웹요청
    #     html2 = xmltodict.parse(html)
    #     res1 = json.dumps(html2)
    #     res2 = json.loads(res1)
    #
    #     data1 = res2['response']
    #     data2 = data1['body']
    #     data3 = data2['items']
    #     data4 = data3['item']
    #     lst = []
    #     for i in data4:
    #         lst.append(i["title"])
    #
    #     return title, data4, lst
