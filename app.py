from flask import Flask, render_template, request
from web_data.flask_practice.for_disabled_sign_lang.bus.bus_main import bp as bus_bp

app = Flask(__name__)

app.secret_key = 'asfaf' #세션 사용시 시크릿 키 설정

#생성한 블루프린트를 flask 객체에 등록
app.register_blueprint(bus_bp)

#메인페이지
@app.route("/")
def index():

    return render_template("index.html")

if __name__ == "__main__":
	app.run()

