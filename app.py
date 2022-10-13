from flask import Flask, render_template, request
from slanguage.slanguage import SLanguageService
from bus.bus_main import bp as bus_bp
import requests
from flask import Flask, render_template, request, json, redirect, flash
from For_Disabled_Sign_Lang.slanguage.slanguage import SLanguageService
from For_Disabled_Sign_Lang.bus.bus import BusService

app = Flask(__name__)
sLanguageService = SLanguageService()
busService = BusService()

# 인덱스화면 연결
app.secret_key = 'asfaf'  # 세션 사용시 시크릿 키 설정

# 생성한 블루프린트를 flask 객체에 등록
app.register_blueprint(bus_bp)
# 메인페이지 연결메서드
@app.route("/")
def index():
    return render_template('index.html')

# 수화 메인 연결메서드
@app.route('/sign/main')
def sindex():
    # 수화 전체리스트 numOfRows로 데이터 양 조절가능
    res = sLanguageService.get_all()
    return render_template('sign_main.html', res=res, enumerate=enumerate)


# 버스 메인 연결메서드
@app.route('/bindex')
def bindex():
    # 버스 전체리스트
    res = busService.get_all()
    return render_template('bus_main.html', res=res)

# 상세 수어 페이지연결
@app.route('/search')
def search():
    # 검색한 파라미터
    title = request.args.get('title')

    # 검색 결과 값
    result = sLanguageService.get_by_title()

    # 검색한 파라미터가 수어list에 없을시 예외 처리
    data2 = sLanguageService.get_all()
    list = []
    for i in data2:
        list.append(i["title"])
    if title not in list:
        flash("검색어를 올바르게 입력하세요 : [ Null or 띄어쓰기 or 없는 키워드 ]")
        return redirect('/sign/main')
    return render_template('search.html', result=result, title1=title)

# 카톡 보내는 메서드 - 수화
@app.route('/kakao')
def kakao():
    # input 버튼 파라미터
    kakao = request.args.get('kakao')

    # 수화 title list에 append
    data2 = sLanguageService.get_all()
    data3 = data2
    list = []
    for i in data3:
        list.append(i["title"])

    # input 파라미터와 수화 title 비교
    if kakao in list:
        # 카카오톡 메시지 API
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": "ebaf179106e4af1cf2b6ae595f2ca1ea", ### 발표자가 다시 발급 받아야 할 수도 있음 ###
            "redirect_url": "http://127.0.0.1:5000/sign/main",
            "code": "QjBElQ794BiHJ1Gm3-lZhY3ODgTaVFJfBa-1ljRnVXOZjVtXJmwJEOuyONmvlXMz7iwZPwo9dVwAAAGDzlzWdg" ### 발표자가 다시 발급 받아야 할 수도 있음 ###
        }
        response = requests.post(url, data=data)
        tokens = response.json()

        # kakao_code.json 파일 저장
        with open("kakao_code.json", "w") as fp:
            json.dump(tokens, fp)

        # #토큰 읽어오기
        # with open("kakao_code.json", "r") as fp:
        #     tokens = json.load(fp)





        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        #'U9H6buL9TAMQks1oCSxja8GwUjteLotV_tBaQ_rlCisM0wAAAYPPEvlA'
        # 사용자 토큰
        headers = {
            "Authorization": "Bearer " + 'U9H6buL9TAMQks1oCSxja8GwUjteLotV_tBaQ_rlCisM0wAAAYPPEvlA' ### 유효시간 6시간 / 발표자가 다시 발급 받아야 할 수도 있음  ###
        }

        data = {
            "template_object": json.dumps({"object_type": "text",
                                           "text": kakao,
                                           # "text": data4,
                                           "link": {'web_url': 'http://127.0.0.1:5000/search?title=' + kakao}
                                           })
        }

        response = requests.post(url, headers=headers, data=data)
        print(response.status_code)
        if response.json().get('result_code') == 0:
            print('메시지를 성공적으로 보냈습니다.')
            flash('전송 성공')
        else:
            print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

    else:
        print('검색오류')
        flash("전송 실패")

    return redirect('/sign/main')






if __name__ == '__main__':
    app.run()  # 플라스크 앱 실행
