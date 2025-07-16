from flask import Flask, request, Response #flask를 import한다. 
                #Flask를 import했다는 것은 웹서버 객체를 쓴다는 말.
                #Request를 import했다는 것은 클라이언트가 서버에 보낸 Request 관련 모든 정보를 담고 있다. (URL, header, 파라미터, JSON, form 등 모든 입력데이터 read)
                #Response를 import 했다는 것은 -> 응답의 MIME 타입, 상태 코드, 스트리밍까지 직접 제어하려는 API 적인 성격 (문자열처럼 단순 Return으로 끝나는 게 아니라) 


import os # 파이썬이 운영체제와 상호작용할 수 있게 해주는 표준 라이브러리를 import 해온다. 여기서는 운영체제 설정 언어 정보를 받아오는 데 사용됨.
from io import BytesIO #io 라이브러리에서 "바이트 버퍼"를 가져오는데, 이를 활용하면 디스크에 저장을 하지 않고 음성/이미지 등의 바이너리 데이터를 RAM 상에서 바로 클라이언트로
                       #전송해준다. 디스크에 파일을 저장하고 불러오는 과정이 생략되니까 속도가 빠르고 깨끗함!
from gtts import gTTS #Google Translate의 Text-To-Speech 엔진으로 목소리를 따온다. 아주 간단한 기능만 제공. 속도 조절만 slow=False (기본속도)/ slow=True로 가능하다.

DEFAULT_LANG=os.getenv('DEFAULT_LANG','ko') #이것 때문에 os를 import한 것으로 보임. os.getenv는 운영체제의 환경 변수를 얻어온다. 
                                            # "DEFAULT_LANG" -> 운영체제에서 설정해 놓은 언어값을 가져오는 것. 설정이 되어 있지 않다면 'ko'(한국어로 설정된다는 이야기.)
app = Flask(__name__)  # app이라는 Flask instance를 생성한다. 이 app이라는 instance의 기본 환경은 현재 실행중인 모듈의 이름(__name__)을 기준으로 설정된다.


@app.route("/") # Root page (http://0.0.0.0/80/ )으로 들어갔을 때 home()을 실행한다. @app.route('/') >Flask에게 home() 함수를 ' '안의 URL과 매핑해달라고 요청하는것.
                # "/"부분이 바뀌게 된다면, 예를 들어 @app.route("/speak") 등과 같이 설정되면 http://0.0.0.0/80/speak에서 home()을 실행하게 되는 것이다.
def home ():

    text = "Hello.DevOps? 나는 멋들어진 프로그래머가 되고 싶어서 코딧세이에 지원했는데 지금은 브이에스 코드와 챗GPT사이에 말을 전하는 전령새가 된 기분이야. 아이고, 끔찍해라!"

    lang=request.args.get('lang',DEFAULT_LANG) #request - 클라이언트(브라우저, 앱)가 서버에 보낸 요청 정보. request.args {"lang"="en", "text"="hello" ... } 
                                               #URL 뒤에 lang (예: /ko, en, ja 등), text 등의 query 인자가 있음 그걸 쓰고, 없으면 DEFAULT_LANG으로 Fallback.
                                               #클라이언트가 언어를 지정할 수 있게 함 (예시: http://127.0.0.1:5000/speak?lang=en ), 그게 없으면 DEFAULT_LANG으로.
    fp = BytesIO()                             #RAM 상에 빈 가상 파일(바이트 버퍼) 객체를 하나 만드는데, 그 객체는 fp라는 이름을 가지고 있다.
    gTTS(text,"com",lang).write_to_fp(fp)      # gTTS는 text의 내용을, "com"->미국 서버(기본) 억양으로, lang에 지정된 언어로 읽어준다. cf) co.uk, co.kr 등도 가능
                                               #gTTS가 생성한 mp3 데이터를 방금 만든 BytesIO, "fp"에 바로 기록한다. 이제 fp를 그대로 다른 함수에 저장할 수 있다.
                                               # cf) gTTS.save("파일명.mp3")를 넣으면 디스크에 파일명.mp3가 저장된다.

    return Response(fp.getvalue(), mimetype='audio/mpeg') # Response: Flask가 제공하는 응답(Response) 객체를 직접 생성. return "hello"같이 간단한게 아니라
                                                          # 파일, 바이너리, 특수한 헤더가 들어가기 떄문에 Response 객체를 만들어야 하는 것. 바이너리를 직접 전송한다. 
                                                          # fp.getvalue() -> BytesIO 객제인 'fp' 안에 있는 모든 데이터를 한 번에 꺼내온다.
                                                          # mimetype='audio/mpeg' -> fp안에서 꺼낸 데이터가 오디오/mpeg으로 압축된 (->mp3) 파일이라는 것을 알려줌.
                                                          # 브라우저는 mimetype 이하 형식을 보고 미디어 플레이어를 띄우거나 다운로드 창을 띄울 지 결정한다.
                                                          # Response 대신: send_file(fp, mimetype='audio/mpeg')을 쓰면 Flask가 알아서 파일 스트리밍을 처리한다.

if __name__ == '__main__': #해당 script가 자체적으로 실행된 거라면 (호출등으로 실행된 경우의 __name__ = app.py)
    app.run('0.0.0.0', 80) #0.0.0.0 (모든 주소), 포트 80으로 서버를 열어준다.


## fp.getvalue로 바이너리를 직접 보내기 때문에, mimetype 값이 달라지면 깨진 문자나 노이즈 등이 출력되거나 에러가 나온다. (바이너리를 어떻게 읽을 건지 헤더로서 기능)
## mimetype: text/plain, text/css, application/javascript, text/csv, image/jpeg, image/png, audio/wav, audio/ogg, video/mp4, video/webm 등 다양하게 있다!