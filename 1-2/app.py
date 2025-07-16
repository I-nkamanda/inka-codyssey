
from flask import Flask #flask 모듈에서 Flask class를 import

app = Flask(__name__) # Flask 앱 객체 생성

@app.route("/") #기본 주소로 접속했을 때
def hello_world(): #실행할 함수의 정의
    return "Hello, DevOps!" #browser에 이 문자열 반환

print(type(app)) #app의 변수 확인해보기 위한 출력


if __name__ == "__main__": #이 파일이 직접 실행될 때만 (호출시 __name__ = app 이다)
    app.run(host="0.0.0.0", port=8080) #서버 시작, (0.0.0.0)--> 모든 IP에서 접근 가능, 포트 =8080