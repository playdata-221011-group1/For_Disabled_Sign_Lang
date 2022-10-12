import requests
from flask import Flask, render_template, request, json, redirect, flash
from For_Disabled_Sign_Lang.slanguage.slanguage import SLanguageService
from For_Disabled_Sign_Lang.bus.bus import BusService

app = Flask(__name__)
app.secret_key = 'asdf'
sLanguageService = SLanguageService()
busService = BusService()


# 인덱스화면 연결

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sindex')
def sindex():
    res = sLanguageService.get_all()
    return render_template('sindex.html', res=res, enumerate=enumerate)


@app.route('/bindex')
def bindex():
    res = busService.get_all()
    return render_template('bindex.html', res=res)


# 상세 수어 페이지연결
@app.route('/search')
def search():
    title = request.args.get('title')
    result = sLanguageService.get_by_title()
    return render_template('search.html', result=result, title1=title)


# 카톡 테스트
@app.route('/kakao')
def kakao():
    kakao = request.args.get('kakao')
    print(kakao)
    data2 = sLanguageService.get_all()
    data3 = data2
    list = []
    for i in data3:
        list.append(i["title"])

    if kakao in list:
        # 카카오톡 메시지 API
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": "8942390846940f8918570a9c142941a3",
            "redirect_url": "http://127.0.0.1:5000/sindex",
            "code": "e3L2uh4k2tfrdjgwRAdzaSq8-uNPjOB1NYB5PC-gYXTNDz7SkV8yEsnbYBaNEYsVHY5Ftgo9dRsAAAGDyxQVCQ"
        }
        response = requests.post(url, data=data)
        tokens = response.json()
        # print(tokens)

        # kakao_code.json 파일 저장
        with open("slanguage/kakao_code.json", "w") as fp:
            json.dump(tokens, fp)

        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

        # 사용자 토큰
        headers = {
            "Authorization": "Bearer " + 'Tr2xtJhc9KjZXiojpG_kWgkNVVrkhi5iVkV4WXnaCilv1AAAAYPLVL6Y'
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

    return redirect('/sindex')


if __name__ == '__main__':
    app.run()  # 플라스크 앱 실행
