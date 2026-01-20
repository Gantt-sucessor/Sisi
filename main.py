#INICIAR ULTRON

#carregar identidade
#carregar memória

#ENQUANTO Ultron estiver ativo:
#    receber entrada do usuário
#    interpretar entrada (percepção)
#    decidir o que fazer (decisão)
#    executar resposta ou ação
#    registrar resultado na memória

#ENCERRAR ULTRON

#SE entrada contém "cansado":
#    resposta = sugerir pausa
#SENÃO:
#    resposta = sugerir continuar


import json

# ---- CARREGAMENTO DE CONFIGURAÇÕES ----

def carregarIdentidade():
    with open("config/identity.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
def carregarMemoria():
    try:
        with open("memory/memory.json", "r", encoding="utf-8") as f:
            conteudo = f.read().strip()

            if not conteudo:
                return {}
            return json.loads(conteudo)
        
    except FileNotFoundError:
        return {}
    
# ---- LOOP----

def receberEntrada():
    return input("Você -> ")

def interpretarEntrada(entrada):
    return entrada.lower()


def decidirAcao(interpretacao):
    if "cansado" in interpretacao:
        return "Não se maltrate, fiquei bem por um tempo"
    return "Continue indo meu mano. Um passo de cada vez."

def executarAcao(resposta):
    print(f"Sisi: {resposta}")

def registrarMemoria(memoria, entrada, resposta):
    memoria["ultima_entrada"] = entrada
    memoria["ultima_resposta"] = resposta

    with open("memory/memory.json", "w", encoding="utf-8") as f:
        json.dump(memoria, f, indent=2, ensure_ascii=False)

def encerrarSisi():
    print("Encerrando Sisi")

# ---- MAIN ----

def iniciarSisi():
    print("Iniciando Sisi...")

    identidade = carregarIdentidade()
    memoria = carregarMemoria()

    print(f"{identidade["nome"]} online")
    ativo = True

    while ativo:
        entrada = receberEntrada()

        if entrada.lower() in ["sair", "encerrar", "fechar"]:
            ativo = False
            break

        interpretacao = interpretarEntrada(entrada)
        decisao = decidirAcao(interpretacao)
        executarAcao(decisao)
        registrarMemoria(memoria, entrada, decisao)

    encerrarSisi()

if __name__ == "__main__":
    iniciarSisi()