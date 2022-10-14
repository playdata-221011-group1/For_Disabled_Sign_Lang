import requests
from flask import render_template, request, Blueprint, flash, redirect, json
from .bus_service import BusService , LowBusService

bus_service = BusService()
low_service = LowBusService()

bp = Blueprint('bus', __name__, url_prefix='/bus')

@bp.route("/main")
def bus_main():
    trans = bus_service.trans_list()

    return render_template("bus_main.html", trans=trans)


# 정거장 검색하면 해당정류장에 정차하는 버스 뿌려주는 메서드
@bp.route('/station')
def low_bus():
    station = request.args.get('station')
    low_list = low_service.getBusStopName()

    # input에 입력된 station과 전체 정류장리스트를 비교해서 유효성 검사
    data = low_service.low_bus_list()
    stationList = []
    for i in data:
        stationList.append(i['stNm'])

    # print(stationList)

    # station 검색 유효성검사
    if station in stationList:
        ###### 버스검색 잘된경우(input의 파라미터가 stationList에 포함된경우) 카카오톡 전송 ######
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": "ebaf179106e4af1cf2b6ae595f2ca1ea",  ### 발표자가 다시 발급 받아야 할 수도 있음 ###
            "redirect_url": "http://127.0.0.1:5000/sign/main",
            "code": "QjBElQ794BiHJ1Gm3-lZhY3ODgTaVFJfBa-1ljRnVXOZjVtXJmwJEOuyONmvlXMz7iwZPwo9dVwAAAGDzlzWdg"
            ### 발표자가 다시 발급 받아야 할 수도 있음 ###
        }
        response = requests.post(url, data=data)
        tokens = response.json()

        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        # 사용자 토큰
        headers = {
            "Authorization": "Bearer " + 'FNFNutUz2EN-Rk-D4AuOVZQ_0TiJFrtQ0m1wtQRnCj10lwAAAYPTqzCP'
            ### 유효시간 6시간 / 발표자가 다시 발급 받아야 할 수도 있음  ###
        }

        data = {
            "template_object": json.dumps({"object_type": "text",
                                           "text": station + '에 정차하는 버스 목록' + '\n' + str(low_list),
                                           # "text": data4,
                                           "link": {'web_url': 'http://127.0.0.1:5000/bus/main'}
                                           })
        }

        response = requests.post(url, headers=headers, data=data)
        print(response.status_code)
        if response.json().get('result_code') == 0:
            print('메시지를 성공적으로 보냈습니다.')
            flash('카카오톡이 성공적으로 전송되었습니다.')
        else:
            print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
            flash("카카오톡 전송 실패")
            return redirect('/bus/main')

        # pass

    elif station == "":
        flash("검색어를 입력하세요 : [ Null ]")
        return redirect('/bus/main')

    elif station not in stationList:
        flash("존재하지 않는 정류장 or 정류장 이름이 다릅니다!!")
        return redirect('/bus/main')

    return render_template('bus_low.html', low=low_list, station=station )


# 버스정류장 리스트 뿌려주는 메서드
@bp.route('/station1')
def station_list():
    res = low_service.low_bus_list()
    return render_template('station.html', res=res)

# @bp.route('/kakao')
# def send_kakao():
#     station = request.args.get('station')
#     low_list = low_service.getBusStopName()
#
#     # input에 입력된 station과 전체 정류장리스트를 비교해서 유효성 검사
#     data = low_service.low_bus_list()
#     stationList = []
#     for i in data:
#         stationList.append(i['stNm'])
#
#     if station in stationList:
#         ###### 버스검색 잘된경우(input의 파라미터가 stationList에 포함된경우) 카카오톡 전송 ######
#         url = "https://kauth.kakao.com/oauth/token"
#         data = {
#             "grant_type": "authorization_code",
#             "client_id": "ebaf179106e4af1cf2b6ae595f2ca1ea",  ### 발표자가 다시 발급 받아야 할 수도 있음 ###
#             "redirect_url": "http://127.0.0.1:5000/sign/main",
#             "code": "QjBElQ794BiHJ1Gm3-lZhY3ODgTaVFJfBa-1ljRnVXOZjVtXJmwJEOuyONmvlXMz7iwZPwo9dVwAAAGDzlzWdg"
#             ### 발표자가 다시 발급 받아야 할 수도 있음 ###
#         }
#         response = requests.post(url, data=data)
#         tokens = response.json()
#
#         url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
#         # 사용자 토큰
#         headers = {
#             "Authorization": "Bearer " + 'FNFNutUz2EN-Rk-D4AuOVZQ_0TiJFrtQ0m1wtQRnCj10lwAAAYPTqzCP'
#             ### 유효시간 6시간 / 발표자가 다시 발급 받아야 할 수도 있음  ###
#         }
#
#         data = {
#             "template_object": json.dumps({"object_type": "text",
#                                            "text": station + '에 정차하는 버스 목록' + '\n' + str(low_list),
#                                            # "text": data4,
#                                            "link": {'web_url': 'http://127.0.0.1:5000/bus/main'}
#                                            })
#         }
#
#         response = requests.post(url, headers=headers, data=data)
#         print(response.status_code)
#         if response.json().get('result_code') == 0:
#             print('메시지를 성공적으로 보냈습니다.')
#             flash('카카오톡이 성공적으로 전송되었습니다.')
#         else:
#             print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
#             flash("카카오톡 전송 실패")
#             return redirect('/bus/main')
#
#
#
#
#     return render_template('bus_low.html', low=low_list, station=station )

