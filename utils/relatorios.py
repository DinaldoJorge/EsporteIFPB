# ==========================================================
# SPORTAVALIA PRO V3
# utils/relatorios.py
# PARTE 1
# ==========================================================

from pathlib import Path
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from utils.excel import (
    caminho_atleta,
    ler_cadastro
)

from utils.avaliacao import (
    ler_avaliacao,
    calcular_media,
    classificar_desempenho
)

# ==========================================================
# PASTA DOS RELATÓRIOS
# ==========================================================

PASTA_RELATORIOS = Path("relatorios")
PASTA_RELATORIOS.mkdir(exist_ok=True)

# ==========================================================
# NOME DO PDF
# ==========================================================

def caminho_pdf(nome):

    nome = nome.replace(" ", "_")

    return PASTA_RELATORIOS / f"{nome}.pdf"

# ==========================================================
# DATA
# ==========================================================

def data_atual():

    return datetime.now().strftime("%d/%m/%Y %H:%M")

# ==========================================================
# DADOS DO ATLETA
# ==========================================================

def dados_relatorio(nome):

    cadastro = ler_cadastro(nome)

    avaliacao = ler_avaliacao(nome)

    media = calcular_media(nome)

    classificacao = classificar_desempenho(media)

    return {

        "cadastro": cadastro,

        "avaliacao": avaliacao,

        "media": media,

        "classificacao": classificacao

    }
# ==========================================================
# GERAR CONTEÚDO DO PDF
# ==========================================================

def gerar_pdf(nome):

    dados = dados_relatorio(nome)

    cadastro = dados["cadastro"]

    avaliacao = dados["avaliacao"]

    media = dados["media"]

    classificacao = dados["classificacao"]

    arquivo_pdf = caminho_pdf(nome)

    doc = SimpleDocTemplate(

        str(arquivo_pdf),

        pagesize=A4,

        rightMargin=30,

        leftMargin=30,

        topMargin=30,

        bottomMargin=30

    )

    estilos = getSampleStyleSheet()

    elementos = []

    # ======================================================
    # TÍTULO
    # ======================================================

    titulo = Paragraph(

        "<b>SPORTAVALIA PRO</b><br/>Relatório de Avaliação Física",

        estilos["Title"]

    )

    elementos.append(titulo)

    elementos.append(Spacer(1,20))

    # ======================================================
    # DADOS DO ATLETA
    # ======================================================

    tabela_dados = [

        ["Nome", cadastro.get("nome","")],

        ["Sexo", cadastro.get("sexo","")],

        ["Idade", cadastro.get("idade","")],

        ["Esporte", cadastro.get("esporte","")],

        ["Equipe", cadastro.get("equipe","")],

        ["Treinador", cadastro.get("treinador","")]

    ]

    tabela = Table(

        tabela_dados,

        colWidths=[120,320]

    )

    tabela.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(0,-1),colors.darkgreen),

        ("TEXTCOLOR",(0,0),(0,-1),colors.white),

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("FONTNAME",(0,0),(-1,-1),"Helvetica"),

        ("BOTTOMPADDING",(0,0),(-1,-1),8)

    ]))

    elementos.append(tabela)

    elementos.append(Spacer(1,20))

    # ======================================================
    # RESULTADOS
    # ======================================================

    elementos.append(

        Paragraph(

            "<b>Resultados da Avaliação</b>",

            estilos["Heading2"]

        )

    )

    elementos.append(Spacer(1,10))

    tabela_resultados = [

        ["Velocidade", avaliacao.get("velocidade","")],

        ["Força", avaliacao.get("forca","")],

        ["Resistência", avaliacao.get("resistencia","")],

        ["Flexibilidade", avaliacao.get("flexibilidade","")],

        ["Coordenação", avaliacao.get("coordenacao","")],

        ["Equilíbrio", avaliacao.get("equilibrio","")]

    ]

    resultados = Table(

        tabela_resultados,

        colWidths=[220,100]

    )

    resultados.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),0.5,colors.grey),

        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),

        ("BOTTOMPADDING",(0,0),(-1,-1),8)

    ]))

    elementos.append(resultados)

    elementos.append(Spacer(1,20))
    # ==========================================================
# MÉDIA E CLASSIFICAÇÃO
# ==========================================================

    elementos.append(

        Paragraph(

            f"<b>Média Geral:</b> {media:.2f}",

            estilos["Heading2"]

        )

    )

    elementos.append(

        Paragraph(

            f"<b>Classificação:</b> {classificacao}",

            estilos["Heading3"]

        )

    )

    elementos.append(Spacer(1,20))

# ==========================================================
# OBSERVAÇÕES
# ==========================================================

    observacoes = ""

    if avaliacao:

        observacoes = avaliacao.get("observacoes") or ""

    elementos.append(

        Paragraph(

            "<b>Observações</b>",

            estilos["Heading2"]

        )

    )

    elementos.append(

        Paragraph(

            observacoes if observacoes else "Nenhuma observação registrada.",

            estilos["BodyText"]

        )

    )

    elementos.append(Spacer(1,20))

# ==========================================================
# RODAPÉ
# ==========================================================

    elementos.append(

        Paragraph(

            f"Relatório gerado em: {data_atual()}",

            estilos["BodyText"]

        )

    )

    elementos.append(Spacer(1,10))

    elementos.append(

        Paragraph(

            "<b>SportAvalia PRO V3</b><br/>"

            "Professor Dinaldo Guedes<br/>"

            "IFPB",

            estilos["Normal"]

        )

    )

# ==========================================================
# GERAR PDF
# ==========================================================

    doc.build(elementos)

    return arquivo_pdf


# ==========================================================
# VERIFICAR EXISTÊNCIA
# ==========================================================

def pdf_existe(nome):

    return caminho_pdf(nome).exists()


# ==========================================================
# RETORNAR CAMINHO
# ==========================================================

def obter_pdf(nome):

    arquivo = caminho_pdf(nome)

    if arquivo.exists():

        return arquivo

    return None


# ==========================================================
# REMOVER PDF
# ==========================================================

def excluir_pdf(nome):

    arquivo = caminho_pdf(nome)

    if arquivo.exists():

        arquivo.unlink()

        return True

    return False


# ==========================================================
# FIM DO ARQUIVO
# ==========================================================