from flask import Flask, jsonify, request
from pymemcache.client import base

servico = Flask(__name__)

BANCO_VOLATIL = "banco_volatil"

# "constantes"
IS_ALIVE = "yes"
VERSION = "0.0.1"
DESCRIPTION = "Servico que retorna noticias e roadmap dos jogos NFT"
AUTHOR = "Bruno Martin Costa Sacramento"
EMAIL = "brunogox9@gmail.com"

# rotas do meu servico
# rota de ping (o cliente deve perguntar se o servico estah atendendo)
@servico.route("/isalive/")
def is_alive():
    return IS_ALIVE


# rota que retorna informacoes basicas sobre o servico e o autor do servico
@servico.route("/info/")
def get_info():
    info = jsonify(
        version = VERSION,
        description = DESCRIPTION, 
        author = AUTHOR,
        email = EMAIL
    )

    return info

@servico.route("/gravar/", methods=["POST", "GET"])
def gravar():
    noticias = request.get_json()
    if noticias:
        client = base.Client((BANCO_VOLATIL, 11211))
        client.set("roadmap", noticias)

    return "Ok"

# rota que retorna noticias sobre sites 
@servico.route("/noticias/")
def get_roadmap():
    resultado = "erro: noticias nao inicializadas"

    client = base.Client((BANCO_VOLATIL, 11211))
    noticias = client.get("roadmap")
    if noticias:
        resultado = noticias

    return resultado

if __name__ == "__main__":
    servico.run(
        host = "0.0.0.0",
        debug=True
    )