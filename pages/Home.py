import streamlit as st
from pathlib import Path
from utils.excel import resumo

# ==========================================================
# SPORTAVALIA PRO V2
# HOME
# ==========================================================
st.markdown("""
<div style="
background:linear-gradient(90deg,#0EA5E9,#0284C7);
padding:16px;
border-radius:15px;
border:2px solid #38BDF8;
box-shadow:0 0 20px rgba(14,165,233,.45);
margin-bottom:25px;
">

<h3 style="color:white;margin:0;">
📱 MENU
</h3>

<p style="
color:white;
font-size:18px;
margin-top:10px;
margin-bottom:0;
">

👈 <b>Toque no botão « MENU » localizado no canto superior esquerdo para abrir a navegação do SportAvalia PRO.</b>

</p>

</div>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="SportAvalia PRO",
    page_icon="🏆",
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
    info = resumo()
    total = info.get("total", 0)
except:
    total = 0

# ==========================================================
# CABEÇALHO
# ==========================================================

st.markdown("""
<div class="titulo-principal">
🏆 SportAvalia PRO
</div>

<div class="subtitulo">
Sistema Inteligente de Avaliação Esportiva
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# INDICADORES
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👥 Atletas",
        total
    )

with c2:
    st.metric(
        "📊 Avaliações",
        "0"
    )

with c3:
    st.metric(
        "🏆 Esportes",
        "0"
    )

with c4:
    st.metric(
        "📄 Relatórios",
        "0"
    )

st.divider()

# ==========================================================
# APRESENTAÇÃO
# ==========================================================

st.markdown("""
## 🚀 Bem-vindo ao SportAvalia PRO

O **SportAvalia PRO** é um sistema desenvolvido em **Python + Streamlit + Excel**
para auxiliar treinadores, professores e profissionais da área esportiva.

O sistema permite:

- 👤 Cadastro de atletas
- 🏃 Controle esportivo
- 📋 Avaliações físicas
- 📊 Dashboard estatístico
- 📈 Gráficos automáticos
- 📄 Relatórios em PDF
- 💾 Armazenamento em Excel

---

### 📌 Situação do Projeto

""")

# ==========================================================
# STATUS
# ==========================================================

st.success("🟢 Sistema iniciado")

st.success("🟢 Excel conectado")

st.info("🔵 Cadastro funcionando")

st.info("🔵 Atletas funcionando")

st.warning("🟡 Dashboard em desenvolvimento")

st.warning("🟡 Avaliações em desenvolvimento")

st.warning("🟡 Relatórios em desenvolvimento")

st.divider()

# ==========================================================
# ROADMAP
# ==========================================================

st.subheader("🛣 Roadmap do Curso")

st.progress(0.45)

st.write("**45% do projeto concluído**")

st.markdown("""

### Módulos

✅ Estrutura

✅ Cadastro

✅ Excel

✅ Atletas

🟡 Dashboard

🟡 Avaliações

🟡 Relatórios

🟡 Finalização

""")

st.divider()

# ==========================================================
# VERSÃO
# ==========================================================

c1, c2 = st.columns(2)

with c1:

    st.info("""
### 🏆 SportAvalia PRO

Versão

**2.0**

Projeto desenvolvido durante o curso.
""")

with c2:

    st.success("""
### 👨‍🏫 Desenvolvedor

Professor

**Dinaldo Guedes**

Instituto Federal da Paraíba
""")

st.divider()

st.caption("SportAvalia PRO • Python • Streamlit • Excel • IFPB")
