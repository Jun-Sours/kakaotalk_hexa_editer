#kakao talk hexa_editer

import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/send?template_id=43550"
user_token ="HYjzYyczoZIvZ47xeAimjc6p7pwMGK8PzjRbWQopcBMAAAF2p9958g"
# 사용자 토큰
headers = {
    "Authorization": "Bearer " + user_token
}

payload = {
    'template_id' : {43550},
    'template_args' : '{"name": "테스트 제목"}'
}
# 카카오톡 메시지 전송
response = requests.post(url, headers=headers, data=payload)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))


text_message = input()

hex_text = text_message.encode("hex")

print(hex_text)