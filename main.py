import pandas as pd
import datetime
from datetime import timedelta
import requests
import json

TimeDate = datetime.date.today()

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)

f_url = "https://kapi.kakao.com/v1/api/talk/friends"
sendurl = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

header = {
    "Authorization": "Bearer " + tokens["access_token"]
}

result = json.loads(requests.get(f_url, headers=header).text)
friends_list = result.get("elements")
friend_id = friends_list[0].get("uuid")

def Timeset():
    today = datetime.date.today()  # 오늘 날짜
    tomorrow = today + timedelta(days=1)  # 내일 날짜
    startDate = today.strftime('%Y%m%d') #간략화
    endDate = tomorrow.strftime('%Y%m%d') #간략화

    url = 'http://52.231.67.67:3000/api/sensorData/duration?deviceNo=414&startDate=' + startDate + '&endDate=' + endDate
    df = pd.read_json(url)
    dataNow = df.loc[0]
    return dataNow
dataNow = Timeset()

def r_data():
    now = datetime.datetime.now()
    data = {
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type": "text",
            "text": now.strftime('%Y-%m-%d %H:%M') + "에 출근하였습니다",
            "link": {
                "web_url": "https://example.com/oauth"
            }
        })
    }
    return data
data = r_data()

while 1:
    now = datetime.datetime.now()
    today = datetime.date.today()  # 오늘 날짜
    tomorrow = today + timedelta(days=1)  # 내일 날짜
    startDate = today.strftime('%Y%m%d') #간략화
    endDate = tomorrow.strftime('%Y%m%d') #간략화

    data = {
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type": "text",
            "text": now.strftime('%Y-%m-%d %H:%M') +"에 출근하였습니다",
            "link": {
                "web_url": "https://example.com/oauth"
            }
        })
    }

    url = 'http://52.231.67.67:3000/api/sensorData/duration?deviceNo=414&startDate=' + startDate + '&endDate=' + endDate
    df = pd.read_json(url)
    dataNow = df.loc[0]

    if dataNow['hr'] > 0:
        response = requests.post(sendurl, headers=header, data=data)
        response.status_code
        print("문자보냄")
        break

while 1:
    now = datetime.datetime.now()
    today = datetime.date.today()  # 오늘 날짜
    tomorrow = today + timedelta(days=1)  # 내일 날짜
    startDate = today.strftime('%Y%m%d') #간략화
    endDate = tomorrow.strftime('%Y%m%d') #간략화

    data = {
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type": "text",
            "text": now.strftime('%Y-%m-%d %H:%M') +"에 출근하였습니다",
            "link": {
                "web_url": "https://example.com/oauth"
            }
        })
    }

    url = 'http://52.231.67.67:3000/api/sensorData/duration?deviceNo=414&startDate=' + startDate + '&endDate=' + endDate

    df = pd.read_json(url)

    dataNow = df.loc[0]

    if TimeDate.strftime('%Y%m%d') != datetime.date.today().strftime('%Y%m%d'):
        TimeDate = TimeDate + timedelta(days=1)
        while 1:
            if dataNow['hr'] > 0:
                response = requests.post(sendurl, headers=headers, data=data)
                response.status_code
                break
            elif TimeDate.strftime('%Y%m%d') != datetime.date.today().strftime('%Y%m%d'):
                break
