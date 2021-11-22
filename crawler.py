import requests
import json
from time import sleep

NOTICIAS_SITE = "noticias/site.json"
NOTICIAS_COIN = "noticias/coin.json"
NOTICIAS_ROADMAP = "noticias/roadmap.json"

URL_SITE = "http://localhost:5001/gravar/"
URL_COIN = "http://localhost:5002/gravar/"
URL_ROADMAP = "http://localhost:5003/gravar/"

def enviar(url, json_noticias):
    arquivo = open(json_noticias, "r")
    dados = json.load(arquivo)
    arquivo.close()

    resposta = "nenhuma noticias para enviar"
    if dados:
        resposta = requests.post(url, json=json.dumps(dados))
        if resposta.ok:
            resposta = "noticias enviadas"
        else:
            resposta = "erro de envio: " + resposta.text

    return resposta


if __name__ == "__main__":
    while True:
        
        resposta = enviar(URL_SITE, NOTICIAS_SITE)
        print(resposta, "[SITE]")

        resposta = enviar(URL_COIN, NOTICIAS_COIN)
        print(resposta, "[COIN]")

        resposta = enviar(URL_ROADMAP, NOTICIAS_ROADMAP)
        print(resposta, "[ROADMAP]")

        sleep(10)