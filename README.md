## 반달곰 커피 홈페이지
[참조링크](https://반달곰커피)
오디오 출력 소스코드
'''
lang=request.args.get('lang',DEFAULT_LANG)
fp=BytesIO()
gTTS(text,"com",lang).write_to_fp(fp)
encoded_audio_data=base64.b64encode(fp.getvalue())
'''
![david](https://github.com/user-attachments/assets/2b08d19f-4211-4bdc-9eab-886dc4988b38)
