#kakao talk hexa_message_editer

import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/send?template_id=43550"
user_token ="b27c9b98fc8ac23154dfd49dafe25217"
# 사용자 토큰
headers = {
    "Authorization": "Bearer " + user_token
}

def mesaage_box(hex_message):
    payload = {
        'template_id' : {43550},
        'template_args' : {'${text}': str(hex_message)}
    }
    return payload

def send_message(hex_message,headers):# 카카오톡 메시지 전송
    payload = mesaage_box(hex_message)
    #payload['template_args'][name]
    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

def input_encoding():
    text_message = input()
    hex_message = text_message.encode('UTF-8-SIG').hex()
    return hex_message

if __name__ == "__main__":
    hex_message = input_encoding()
    send_message(hex_message,headers)

