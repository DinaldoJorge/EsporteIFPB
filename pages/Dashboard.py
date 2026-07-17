# ==========================================================
# SPORTAVALIA PRO V2
# DASHBOARD
# PARTE 1
# ==========================================================

import streamlit as st

from pathlib import Path

from utils.dashboard import (
    indicadores_dashboard,
    resumo_dashboard
)

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
# Espaço após configurar a página
st.write("")
st.write("")
st.write("")

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
# DADOS
# ==========================================================

try:

    indicadores = indicadores_dashboard()

    dashboard = resumo_dashboard()

except Exception as erro:

    st.error("Erro ao carregar Dashboard.")

    st.exception(erro)

    st.stop()

# ==========================================================
# CABEÇALHO
# ==========================================================

st.title("📊 Dashboard")

st.caption("SportAvalia PRO V2")

st.divider()

# ==========================================================
# INDICADORES
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "👥 Atletas",
        indicadores["total"]
    )

with c2:

    st.metric(
        "🎂 Média Idade",
        indicadores["idade_media"]
    )

with c3:

    st.metric(
        "⚖️ IMC Médio",
        indicadores["imc_medio"]
    )

with c4:

    st.metric(
        "🏆 Esportes",
        indicadores["esportes"]
    )

st.divider()

# ==========================================================
# TÍTULO
# ==========================================================

st.subheader("📈 Estatísticas do Sistema")
# ==========================================================
# RANKING + ÚLTIMOS ATLETAS
# ==========================================================

col1, col2 = st.columns([2, 1])

# ==========================================================
# RANKING DOS ESPORTES
# ==========================================================

with col1:

    st.markdown("### 🏆 Ranking dos Esportes")

    ranking = dashboard["ranking"]

    if len(ranking) == 0:

        st.info("Nenhum atleta cadastrado.")

    else:

        posicao = 1

        for esporte, quantidade in ranking:

            medalha = "🏅"

            if posicao == 1:
                medalha = "🥇"

            elif posicao == 2:
                medalha = "🥈"

            elif posicao == 3:
                medalha = "🥉"

            st.metric(
                f"{medalha} {esporte}",
                quantidade
            )

            posicao += 1

# ==========================================================
# STATUS
# ==========================================================

with col2:

    st.markdown("### ⚙️ Sistema")

    st.success("🟢 Sistema Online")

    st.success("🟢 Excel")

    st.success("🟢 Cadastro")

    st.success("🟢 Dashboard")

    st.info(
        f"Último atleta\n\n**{dashboard['ultimo']}**"
    )

# ==========================================================
# ÚLTIMOS ATLETAS
# ==========================================================

st.divider()

st.subheader("👥 Últimos Atletas")

ultimos = dashboard["ultimos"]

if len(ultimos) == 0:

    st.warning("Nenhum atleta encontrado.")

else:

    for atleta in ultimos:

        with st.container(border=True):

            c1, c2, c3, c4 = st.columns([3,2,2,2])

            with c1:

                st.write(
                    f"### 👤 {atleta['nome']}"
                )

            with c2:

                st.write(
                    f"🏆 {atleta['esporte']}"
                )

            with c3:

                st.write(
                    f"🎂 {atleta['idade']} anos"
                )

            with c4:

                st.write(
                    f"⚖️ IMC {atleta['imc']}"
                )

st.divider()
# ==========================================================
# GRÁFICO
# ==========================================================

st.subheader("📊 Distribuição dos Esportes")

nomes, valores = dashboard["grafico"]

if len(nomes) > 0:

    try:

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(9,4))

        ax.bar(
            nomes,
            valores
        )

        ax.set_title("Atletas por Esporte")

        ax.set_xlabel("Esporte")

        ax.set_ylabel("Quantidade")

        plt.xticks(rotation=20)

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    except Exception as erro:

        st.error("Erro ao gerar gráfico.")

        st.exception(erro)

else:

    st.info("Cadastre atletas para visualizar o gráfico.")

# ==========================================================
# RESUMO GERAL
# ==========================================================

st.divider()

st.subheader("📈 Resumo Geral")

c1, c2, c3 = st.columns(3)

with c1:

    st.info(f"""
### 👥 Atletas

**{indicadores['total']}**
""")

with c2:

    st.info(f"""
### 🎂 Idade Média

**{indicadores['idade_media']} anos**
""")

with c3:

    st.info(f"""
### ⚖️ IMC Médio

**{indicadores['imc_medio']}**
""")

# ==========================================================
# INFORMAÇÕES
# ==========================================================

st.divider()

with st.expander("ℹ️ Sobre este Dashboard"):

    st.markdown("""

Este painel apresenta automaticamente:

- 👥 Total de atletas

- 🎂 Média das idades

- ⚖️ Média do IMC

- 🏆 Ranking dos esportes

- 📊 Gráfico estatístico

- 👤 Últimos atletas cadastrados

Todos os dados são carregados diretamente das
planilhas Excel do SportAvalia PRO.

""")

# ==========================================================
# STATUS
# ==========================================================

st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("🟢 Sistema")

with c2:
    st.success("🟢 Excel")

with c3:
    st.success("🟢 Cadastro")

with c4:
    st.success("🟢 Dashboard")

# ==========================================================
# RODAPÉ
# ==========================================================

st.divider()

st.caption(
    "🏆 SportAvalia PRO V2 • Dashboard • Python • Streamlit • Excel • Professor Dinaldo Guedes • IFPB"
)