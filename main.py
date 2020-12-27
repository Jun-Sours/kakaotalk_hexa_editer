#kakao talk hexa_editer

import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
user_token ="ZX-TmIs1Eny9RtR9Ni1J58h2x7cN71VTLy32OAopyV8AAAF2pUes_w"
# 사용자 토큰
headers = {
    "Authorization": "Bearer " + user_token
}

payload = {
    "template_object" : {"object_type": "feed"},
    "template_id" : {43551},
    "template_arg" : '{"name":"안녕하세요."}'
    }
# 카카오톡 메시지 전송
response = requests.post(url, headers=headers, data=payload)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
