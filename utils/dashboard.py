# ==========================================================
# SPORTAVALIA PRO V2
# DASHBOARD
# PARTE 1
# ==========================================================

from collections import Counter

from utils.excel import listar_dados_atletas

# ==========================================================
# CARREGAR
# ==========================================================

def carregar():

    return listar_dados_atletas()


# ==========================================================
# TOTAL
# ==========================================================

def total_atletas():

    return len(carregar())


# ==========================================================
# MÉDIA IDADE
# ==========================================================

def media_idade():

    atletas = carregar()

    if not atletas:

        return 0

    soma = 0

    quantidade = 0

    for atleta in atletas:

        idade = atleta.get("idade")

        if idade is not None:

            soma += idade

            quantidade += 1

    if quantidade == 0:

        return 0

    return round(soma / quantidade, 1)


# ==========================================================
# MÉDIA IMC
# ==========================================================

def media_imc():

    atletas = carregar()

    if not atletas:

        return 0

    soma = 0

    quantidade = 0

    for atleta in atletas:

        imc = atleta.get("imc")

        if imc is not None:

            soma += imc

            quantidade += 1

    if quantidade == 0:

        return 0

    return round(soma / quantidade, 2)


# ==========================================================
# ESPORTES
# ==========================================================

def esportes():

    atletas = carregar()

    contador = Counter()

    for atleta in atletas:

        esporte = atleta.get("esporte", "Não informado")

        contador[esporte] += 1

    return dict(contador)
# ==========================================================
# RANKING DOS ESPORTES
# ==========================================================

def ranking_esportes():

    dados = esportes()

    return sorted(
        dados.items(),
        key=lambda x: x[1],
        reverse=True
    )


# ==========================================================
# ÚLTIMOS ATLETAS
# ==========================================================

def ultimos_atletas(limite=10):

    atletas = carregar()

    if not atletas:

        return []

    return atletas[-limite:][::-1]


# ==========================================================
# DADOS DO GRÁFICO
# ==========================================================

def dados_grafico():

    dados = esportes()

    nomes = list(dados.keys())

    valores = list(dados.values())

    return nomes, valores


# ==========================================================
# INDICADORES
# ==========================================================

def indicadores_dashboard():

    return {

        "total": total_atletas(),

        "idade_media": media_idade(),

        "imc_medio": media_imc(),

        "esportes": len(esportes())

    }


# ==========================================================
# RESUMO
# ==========================================================

def resumo_dashboard():

    atletas = carregar()

    if atletas:

        ultimo = atletas[-1].get("nome", "")

    else:

        ultimo = "Nenhum"

    return {

        "indicadores": indicadores_dashboard(),

        "ranking": ranking_esportes(),

        "ultimos": ultimos_atletas(),

        "grafico": dados_grafico(),

        "ultimo": ultimo

    }


# ==========================================================
# STATUS
# ==========================================================

def status_sistema():

    return {

        "sistema": True,

        "excel": True,

        "cadastro": True,

        "dashboard": True

    }


# ==========================================================
# FIM DO ARQUIVO
# ==========================================================