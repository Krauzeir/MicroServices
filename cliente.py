import urllib.request
import json
import time

# rotas do servico de site
SITE_URL_SERVICO = "http://localhost:5001/"
SITE_IS_ALIVE = SITE_URL_SERVICO + "isalive/"
SITE_NOTICIAS = SITE_URL_SERVICO + "noticias/"

# rotas do servico de coin
COIN_URL_SERVICO = "http://localhost:5002/"
COIN_IS_ALIVE = COIN_URL_SERVICO + "isalive/"
COIN_NOTICIAS = COIN_URL_SERVICO + "noticias/"

# rotas do servico de roadmap
ROADMAP_URL_SERVICO = "http://localhost:5003/"
ROADMAP_IS_ALIVE = ROADMAP_URL_SERVICO + "isalive/"
ROADMAP_NOTICIAS = ROADMAP_URL_SERVICO + "noticias/"



def acessar(url):
    print("acessando a url:", url)

    response = urllib.request.urlopen(url)
    data = response.read()

    return data.decode("utf-8")

def site_is_alive():
    alive = False

    if acessar(SITE_IS_ALIVE) == "yes":
        alive = True

    return alive

def coin_is_alive():
    alive = False

    if acessar(COIN_IS_ALIVE) == "yes":
        alive = True

    return alive

def roadmap_is_alive():
    alive = False

    if acessar(ROADMAP_IS_ALIVE) == "yes":
        alive = True

    return alive

def get_site():
    data = acessar(SITE_NOTICIAS)
    data = json.loads(data)

    return data["noticias"]

def get_coin():
    data = acessar(COIN_NOTICIAS)
    data = json.loads(data)

    return data["noticias"]

def get_roadmap():
    data = acessar(ROADMAP_NOTICIAS)
    data = json.loads(data)

    return data["noticias"]

def imprimir_noticias1(noticias):
    for noticia in noticias:
        print(noticia["titulo"])
        print(noticia["sobre"])
        print("url:", noticia["endereco"])
        print("###############################################################")

def imprimir_noticias2(noticias):
    for noticia in noticias:
        print(noticia["titulo"])
        print(noticia["moeda"])
        print("url:", noticia["valor"])
        print("###############################################################")

def imprimir_noticias3(noticias):
    for noticia in noticias:
        print(noticia["titulo"])
        print(noticia["data"])
        print("url:", noticia["ultimaatt"])
        print("###############################################################")

if __name__ == "__main__":
    while True:
        # verificar se o servico de site esta ativo
        if site_is_alive():
            # se estiver ativo
            print("servico de site esta ativo. Solicitando informacoes...")
            # imprimir as noticias sobre jogos eletronicos
            noticias = get_site()

            print("\n\n")
            print("###############################################################")
            print("#################### JOGOS NFT ########################")
            print("###############################################################")
            imprimir_noticias1(noticias)
        # se nao estiver (ativo) informar que o servico estah inativo
        else:
            print("servico de site nao esta ativo!")

        # verificar se o servico de moedas esta ativo
        if coin_is_alive():
            # se estiver ativo
            print("servico de site esta ativo. Solicitando informacoes...")
            # imprimir as noticias sobre sistemas operacionais
            noticias = get_coin()

            print("\n\n")
            print("###############################################################")
            print("################## INFORMACOES SOBRE MOEDAS ######################")
            print("###############################################################")
            imprimir_noticias2(noticias)
            # se nao estiver, informar que o servico estah inativo
        else:
            print("servico de site nao esta ativo!")

        # verificar se o servico de roadmap estah ativo
        if roadmap_is_alive():
            # se estiver ativo
            print("servico de site esta ativo. Solicitando informacoes...")
            # imprimir as noticias sobre roadmap operacionais
            noticias = get_roadmap()

            print("\n\n")
            print("###############################################################")
            print("################## ULTIMAS ATUALIZACOES ######################")
            print("###############################################################")
            imprimir_noticias3(noticias)
            # se nao estiver, informar que o servico estah inativo
        else:
            print("servico de site nao esta ativo!")

        time.sleep(5)