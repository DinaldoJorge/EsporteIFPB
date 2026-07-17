# ==========================================================
# SPORTAVALIA PRO V2
# Cadastro.py
# PARTE 1
# ==========================================================

import streamlit as st

from pathlib import Path

from datetime import date, datetime

from utils.excel import (
    salvar_cadastro,
    atualizar_cadastro,
    atleta_existe,
    ler_cadastro
)
# Espaço após configurar a página
st.write("")
st.write("")
st.write("")

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

st.set_page_config(
    page_title="Cadastro de Atleta",
    page_icon="🏆",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

css = Path("styles.css")

if css.exists():

    with open(css, encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# FUNÇÕES
# ==========================================================

def calcular_idade(nascimento):

    hoje = date.today()

    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (
        nascimento.month,
        nascimento.day
    ):

        idade -= 1

    return idade


def calcular_imc(peso, altura):

    if altura <= 0:

        return 0

    return round(peso / (altura * altura), 2)


def classificar_imc(imc):

    if imc < 18.5:

        return "🔵 Abaixo do peso"

    elif imc < 25:

        return "🟢 Peso normal"

    elif imc < 30:

        return "🟡 Sobrepeso"

    elif imc < 35:

        return "🟠 Obesidade I"

    elif imc < 40:

        return "🔴 Obesidade II"

    return "⛔ Obesidade III"


def progresso(nome, telefone, email):

    total = 3

    ok = 0

    if nome.strip():

        ok += 1

    if telefone.strip():

        ok += 1

    if email.strip():

        ok += 1

    return ok / total

# ==========================================================
# MODO EDIÇÃO
# ==========================================================

modo = "novo"

dados = {}

if "modo" not in st.session_state:

    st.session_state["modo"] = "novo"

if "atleta_edicao" not in st.session_state:

    st.session_state["atleta_edicao"] = None

if (
    st.session_state["modo"] == "editar"
    and
    st.session_state["atleta_edicao"]
):

    atleta = st.session_state["atleta_edicao"]

    dados = ler_cadastro(atleta)

    if dados:

        modo = "editar"

# ==========================================================
# VALORES PADRÃO
# ==========================================================

def valor(campo, padrao):

    if modo == "editar":

        return dados.get(campo, padrao)

    return padrao

# ==========================================================
# CABEÇALHO
# ==========================================================

st.title("🏆 Cadastro de Atleta")

if modo == "editar":

    st.warning("✏️ Modo de edição")

else:

    st.success("➕ Novo cadastro")

st.caption("SportAvalia PRO V2")

st.divider()

# ==========================================================
# PROGRESSO
# ==========================================================

barra = st.empty()

barra.progress(0)

# ==========================================================
# DADOS PESSOAIS
# ==========================================================

st.subheader("👤 Dados Pessoais")

col1, col2 = st.columns(2)

with col1:

    nome = st.text_input(
        "Nome Completo",
        value=valor("nome", "")
    )

    sexo = st.selectbox(
        "Sexo",
        ["Masculino", "Feminino"],
        index=0 if valor("sexo", "Masculino") == "Masculino" else 1
    )

    nascimento_txt = valor(
        "nascimento",
        "01/01/2010"
    )

    if isinstance(nascimento_txt, str):

        try:

            nascimento = datetime.strptime(
                nascimento_txt,
                "%d/%m/%Y"
            ).date()

        except:

            nascimento = date(2010, 1, 1)

    else:

        nascimento = nascimento_txt

    nascimento = st.date_input(
        "Data de Nascimento",
        nascimento,
        format="DD/MM/YYYY"
    )

    idade = calcular_idade(nascimento)

    st.metric(
        "🎂 Idade",
        f"{idade} anos"
    )

with col2:

    esportes = [

        "Futebol",

        "Futsal",

        "Basquete",

        "Vôlei",

        "Handebol",

        "Atletismo",

        "Natação",

        "Tênis",

        "Judô",

        "Jiu-Jitsu"

    ]

    esporte_padrao = valor(
        "esporte",
        "Futebol"
    )

    indice = 0

    if esporte_padrao in esportes:

        indice = esportes.index(
            esporte_padrao
        )

    esporte = st.selectbox(
        "Esporte",
        esportes,
        index=indice
    )

    posicao = st.text_input(
        "Posição",
        value=valor("posicao", "")
    )

    equipe = st.text_input(
        "Equipe",
        value=valor("equipe", "")
    )

    treinador = st.text_input(
        "Treinador",
        value=valor("treinador", "")
    )
    # ==========================================================
# DADOS FÍSICOS
# ==========================================================

st.divider()

st.subheader("📏 Dados Físicos")

c1, c2, c3 = st.columns(3)

with c1:

    altura = st.number_input(
        "Altura (m)",
        min_value=0.50,
        max_value=2.50,
        value=float(valor("altura", 1.70)),
        step=0.01,
        format="%.2f"
    )

with c2:

    peso = st.number_input(
        "Peso (kg)",
        min_value=20.0,
        max_value=300.0,
        value=float(valor("peso", 70.0)),
        step=0.5
    )

imc = calcular_imc(peso, altura)

with c3:

    st.metric(
        "⚖️ IMC",
        f"{imc:.2f}"
    )

    st.caption(classificar_imc(imc))

# ==========================================================
# AVATAR
# ==========================================================

st.divider()

st.subheader("🧍 Perfil")

avatar1, avatar2 = st.columns([1,4])

with avatar1:

    if sexo == "Masculino":

        st.markdown(
            "<h1 style='text-align:center;'>👨</h1>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            "<h1 style='text-align:center;'>👩</h1>",
            unsafe_allow_html=True
        )

with avatar2:

    st.info(f"""

Nome

**{nome if nome else '---'}**

Esporte

**{esporte}**

Equipe

**{equipe if equipe else '---'}**

""")

# ==========================================================
# CONTATO
# ==========================================================

st.divider()

st.subheader("📞 Contato")

c1, c2 = st.columns(2)

with c1:

    telefone = st.text_input(
        "Telefone",
        value=valor("telefone", "")
    )

with c2:

    email = st.text_input(
        "E-mail",
        value=valor("email", "")
    )

# ==========================================================
# OBSERVAÇÕES
# ==========================================================

st.divider()

st.subheader("📝 Observações")

observacoes = st.text_area(
    "Observações",
    value=valor("observacoes", ""),
    height=140
)

# ==========================================================
# PROGRESSO DO FORMULÁRIO
# ==========================================================

percentual = progresso(
    nome,
    telefone,
    email
)

barra.progress(percentual)

st.caption(
    f"Preenchimento: {int(percentual*100)}%"
)

st.divider()
# ==========================================================
# BOTÕES
# ==========================================================

b1, b2, b3 = st.columns(3)

with b1:

    salvar = st.button(
        "💾 SALVAR CADASTRO",
        use_container_width=True
    )

with b2:

    atualizar = st.button(
        "✏️ ATUALIZAR CADASTRO",
        use_container_width=True,
        disabled=(modo != "editar")
    )

with b3:

    limpar = st.button(
        "🧹 LIMPAR",
        use_container_width=True
    )

# ==========================================================
# LIMPAR
# ==========================================================

if limpar:

    st.session_state.clear()

    st.rerun()

# ==========================================================
# SALVAR
# ==========================================================

if salvar:

    nome = nome.strip()

    if nome == "":

        st.error("Informe o nome do atleta.")

        st.stop()

    if atleta_existe(nome):

        st.warning("Já existe um atleta com este nome.")

        st.stop()

    try:

        salvar_cadastro(

            nome,

            sexo,

            idade,

            nascimento.strftime("%d/%m/%Y"),

            esporte,

            posicao,

            equipe,

            treinador,

            altura,

            peso,

            imc,

            telefone,

            email,

            observacoes

        )

        st.success("✅ Atleta cadastrado com sucesso!")

        st.balloons()

    except Exception as erro:

        st.error("Erro ao salvar cadastro.")

        st.exception(erro)

# ==========================================================
# ATUALIZAR
# ==========================================================

if atualizar:

    try:

        atualizar_cadastro(

            nome,

            sexo,

            idade,

            nascimento.strftime("%d/%m/%Y"),

            esporte,

            posicao,

            equipe,

            treinador,

            altura,

            peso,

            imc,

            telefone,

            email,

            observacoes

        )

        st.success("✅ Cadastro atualizado!")

        st.session_state["modo"] = "novo"

        st.session_state["atleta_edicao"] = None

        st.rerun()

    except Exception as erro:

        st.error("Erro ao atualizar cadastro.")

        st.exception(erro)

# ==========================================================
# RESUMO
# ==========================================================

st.divider()

st.subheader("📋 Resumo")

c1, c2 = st.columns(2)

with c1:

    st.write(f"**👤 Nome:** {nome}")

    st.write(f"**🏆 Esporte:** {esporte}")

    st.write(f"**🎂 Idade:** {idade} anos")

    st.write(f"**🏟 Equipe:** {equipe}")

with c2:

    st.write(f"**📏 Altura:** {altura:.2f} m")

    st.write(f"**⚖ Peso:** {peso:.1f} kg")

    st.write(f"**📊 IMC:** {imc:.2f}")

    st.write(f"**📱 Telefone:** {telefone}")

st.divider()

st.info(
    """
### 🏆 SportAvalia PRO V2

Cadastro Inteligente de Atletas

✔ Cadastro

✔ Edição

✔ IMC Automático

✔ Idade Automática

✔ Excel Integrado
"""
)

st.caption(
    "SportAvalia PRO v2 • Professor Dinaldo Guedes • IFPB"
)