import requests
import json


email = 'matheusmu301@gmail.com'
post_login = 'https://apipf.jogajuntoinstituto.org/login'

login_data = {
    "email": email,
    "password": 'AAAAb'
    }

ordem_login = sorted(login_data.items(),key=lambda x:['email','password'].index(x[0]))
ordem_login = dict(ordem_login)

response = requests.post(post_login,json=ordem_login)
if response.status_code == 200:
    login_response = response.json()
    with open('login_response.json', 'w') as json_file:
        json.dump(login_response,json_file,indent=4)
        print("Resposta do login salva em login_response.json")
else:
    print(f"Erro ao fazer login: {response.text}")

