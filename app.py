import streamlit as st
from pathlib import Path

from utils.excel import resumo

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

st.set_page_config(
    page_title="SportAvalia PRO",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Espaço após configurar a página
st.write("")
st.write("")
st.write("")
# ==========================================================
# CARREGAR CSS
# ==========================================================

css = Path("styles.css")

if css.exists():

    with open(css, encoding="utf-8") as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )

# ==========================================================
# DADOS DO DASHBOARD
# ==========================================================

dados = resumo()

total_atletas = dados.get("total", 0)

ultimo_atleta = dados.get("ultimo") or "-"

# ==========================================================
# TÍTULO
# ==========================================================

st.markdown("""

<div class="titulo-principal">

🏆 SportAvalia PRO

</div>

<div class="subtitulo">

Sistema Inteligente de Avaliação Esportiva

</div>

""",

unsafe_allow_html=True)

st.divider()
# ==========================================================
# DASHBOARD
# ==========================================================

st.subheader("📊 Visão Geral")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(

        "👥 Atletas",

        total_atletas

    )

with col2:

    st.metric(

        "🏃 Último Atleta",

        ultimo_atleta

    )

with col3:

    st.metric(

        "📋 Avaliações",

        "Em desenvolvimento"

    )

with col4:

    st.metric(

        "📄 Relatórios",

        "Em desenvolvimento"

    )

st.divider()

# ==========================================================
# APRESENTAÇÃO
# ==========================================================

st.markdown("""

## 🚀 Bem-vindo ao SportAvalia PRO

O **SportAvalia PRO** é um sistema desenvolvido para facilitar o gerenciamento
de atletas utilizando **Python + Streamlit + Excel**, sem necessidade de banco de dados.

### Funcionalidades já disponíveis

- ✅ Cadastro de atletas
- ✅ Edição de cadastro
- ✅ Lista de atletas
- ✅ Dashboard
- ✅ Avaliação Física
- ✅ Integração com Excel

### Próximas funcionalidades

- 📄 Relatórios em PDF
- 📈 Evolução do atleta
- 📊 Dashboard avançado
- 💾 Backup automático
- 🔐 Login de usuários
- 📦 Exportação de dados

""")
# ==========================================================
# ACESSO RÁPIDO
# ==========================================================

st.divider()

st.subheader("⚡ Acesso Rápido")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### 👥 Cadastro de Atletas

Cadastre novos atletas e mantenha os dados atualizados.

➡ Utilize a página **Cadastro** no menu lateral.
""")

    st.info("""
### 📋 Avaliação Física

Registre velocidade, força, resistência, flexibilidade,
coordenação e equilíbrio.

➡ Utilize a página **Avaliação**.
""")

with c2:

    st.info("""
### 📊 Dashboard

Visualize indicadores e estatísticas gerais dos atletas.

➡ Utilize a página **Dashboard**.
""")

    st.info("""
### 📄 Relatórios

Em breve será possível gerar relatórios em PDF
com gráficos e resultados.

""")

# ==========================================================
# STATUS DO SISTEMA
# ==========================================================

st.divider()

st.subheader("🟢 Status do Sistema")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.success("Excel OK")

with s2:
    st.success("Cadastro OK")

with s3:
    st.success("Avaliação OK")

with s4:
    st.success("Dashboard OK")

# ==========================================================
# SOBRE O PROJETO
# ==========================================================

st.divider()

with st.expander("ℹ️ Sobre o SportAvalia PRO"):

    st.markdown("""

O **SportAvalia PRO** é um sistema desenvolvido para
avaliação esportiva utilizando exclusivamente arquivos Excel.

### Tecnologias

- 🐍 Python
- 🎈 Streamlit
- 📊 OpenPyXL
- 📈 Matplotlib
- 📄 ReportLab

### Objetivos

- Cadastro de atletas
- Avaliações físicas
- Dashboard
- Relatórios em PDF
- Histórico
- Backup
- Exportação

""")

# ==========================================================
# RODAPÉ
# ==========================================================

st.divider()

st.caption(
    "🏆 SportAvalia PRO V3 • Professor Dinaldo Guedes • IFPB • Python • Streamlit • Excel"
)