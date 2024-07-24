import requests
import json

criar_cont_api = 'https://apipf.jogajuntoinstituto.org/register'
email = 'matheusmu301@gmail.com'

cria_cont = {
    "email": email,
    "password": 'AAAAb'
}


ordem_cria_cont = sorted(cria_cont.items(),key=lambda x:['email','password'].index(x[0]))
ordem_cria_cont = dict(ordem_cria_cont)

response = requests.post(criar_cont_api,json=ordem_cria_cont)

if response.status_code == 200:
    print("sucesso!!!!!!!!!!!!!!!!!!!!!!")
    cria_cont_response = response.json()
    with open('cria_cont_response.json','w') as json_file:
        json.dump(cria_cont_response, json_file, indent=4)

    print("json feito com sucesso")
else:
    print(f"deu errado pois{response.text}")

