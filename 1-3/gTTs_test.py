from gtts import gTTS

#변환할 텍스트
text = "가상환경 gTTS 테스트 중이야. 잘 작동하면? 성공인 거지."

#gTTS 객체 생성 (언어는 한국어)

tts = gTTS(text=text, lang='ko')

#mp3파일로 저장
tts.save("gtts_test.mp3")

print("✅ gtts_test.mp3 파일이 생성되었습니다!")


