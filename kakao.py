import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'a2c7c116f5da4fb473a9408781564fdf'
redirect_uri = 'https://example.com/oauth'
authorize_code = 's_PPk-GV77ETBkWeWK34cmsgFFAMKmijO-PgOsQC_pmqRQAFULLMR5lbstxHlPox8IM_NworDKcAAAF_CgWIMw'

data = {
    'grant_type': 'authorization_code',
    'client_id': rest_api_key,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()

with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

