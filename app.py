from flask import Flask, render_template, request
from slanguage.slanguage import SLanguageService
from bus.bus_main import bp as bus_bp

app = Flask(__name__)
sLanguageService = SLanguageService()

# 인덱스화면 연결
app.secret_key = 'asfaf' #세션 사용시 시크릿 키 설정

#생성한 블루프린트를 flask 객체에 등록
app.register_blueprint(bus_bp)

#메인페이지
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/sign/main')
def sindex():
    res = sLanguageService.get_all()
    return render_template('sign_main.html', res=res, enumerate=enumerate)

# 상세 수어 페이지연결
@app.route('/search')
def search():
    title = request.args.get('title')
    result = sLanguageService.get_by_title()
    return render_template('search.html', result=result, title1=title)


if __name__ == '__main__':
    app.run()  # 플라스크 앱 실행