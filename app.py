from flask import Flask, render_template, request
from For_Disabled_Sign_Lang.slanguage.slanguage import SLanguageService

app = Flask(__name__)
sLanguageService = SLanguageService()


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
    return render_template('bindex.html')


# 상세 수어 페이지연결
@app.route('/search')
def search():
    title = request.args.get('title')
    result = sLanguageService.get_by_title()
    return render_template('search.html', result=result, title1=title)


if __name__ == '__main__':
    app.run()  # 플라스크 앱 실행
