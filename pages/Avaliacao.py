# ==========================================================
# SPORTAVALIA PRO V2
# AVALIACAO.PY
# PARTE 1
# ==========================================================

import streamlit as st

from pathlib import Path

from utils.excel import listar_atletas

from utils.avaliacao import (

    ler_avaliacao,

    indicadores_avaliacao

)
# Espaço após configurar a página
st.write("")
st.write("")
st.write("")

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

st.set_page_config(

    page_title="Avaliação Física",

    page_icon="🏋️",

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
# TÍTULO
# ==========================================================

st.title("🏋️ Avaliação Física")

st.caption("SportAvalia PRO V2")

st.divider()

# ==========================================================
# ATLETAS
# ==========================================================

atletas = listar_atletas()

if len(atletas) == 0:

    st.warning(

        "Cadastre um atleta primeiro."

    )

    st.stop()

# ==========================================================
# SELEÇÃO
# ==========================================================

nome = st.selectbox(

    "👤 Atleta",

    atletas

)

dados = ler_avaliacao(nome)

indicadores = indicadores_avaliacao(nome)

st.divider()

# ==========================================================
# INDICADORES
# ==========================================================

c1,c2,c3 = st.columns(3)

with c1:

    st.metric(

        "📊 Média",

        indicadores["media"]

    )

with c2:

    st.metric(

        "🏆 Pontuação",

        indicadores["total"]

    )

with c3:

    st.metric(

        "⭐ Classificação",

        indicadores["classificacao"]

    )

st.divider()

st.subheader("📋 Avaliação Física")
# ==========================================================
# TESTES FÍSICOS
# ==========================================================

col1, col2 = st.columns(2)

# ==========================================================
# COLUNA 1
# ==========================================================

with col1:

    velocidade = st.slider(
        "⚡ Velocidade",
        0,
        10,
        int(dados["velocidade"] or 0)
    )

    forca = st.slider(
        "💪 Força",
        0,
        10,
        int(dados["forca"] or 0)
    )

    resistencia = st.slider(
        "🏃 Resistência",
        0,
        10,
        int(dados["resistencia"] or 0)
    )

# ==========================================================
# COLUNA 2
# ==========================================================

with col2:

    flexibilidade = st.slider(
        "🤸 Flexibilidade",
        0,
        10,
        int(dados["flexibilidade"] or 0)
    )

    coordenacao = st.slider(
        "🧠 Coordenação",
        0,
        10,
        int(dados["coordenacao"] or 0)
    )

    equilibrio = st.slider(
        "⚖️ Equilíbrio",
        0,
        10,
        int(dados["equilibrio"] or 0)
    )

# ==========================================================
# OBSERVAÇÕES
# ==========================================================

st.divider()

observacoes = st.text_area(
    "📝 Observações",
    value=dados["observacoes"] or "",
    height=150
)

# ==========================================================
# RESULTADOS
# ==========================================================

media = round(

    (
        velocidade +
        forca +
        resistencia +
        flexibilidade +
        coordenacao +
        equilibrio
    ) / 6,

    2

)

total = (

    velocidade +
    forca +
    resistencia +
    flexibilidade +
    coordenacao +
    equilibrio

)

# ==========================================================
# CLASSIFICAÇÃO
# ==========================================================

if media >= 9:

    classificacao = "🏆 Excelente"

elif media >= 8:

    classificacao = "🥇 Muito Bom"

elif media >= 7:

    classificacao = "🥈 Bom"

elif media >= 6:

    classificacao = "🥉 Regular"

elif media >= 5:

    classificacao = "⚠ Em desenvolvimento"

else:

    classificacao = "❌ Necessita treinamento"

# ==========================================================
# DASHBOARD
# ==========================================================

st.divider()

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "📊 Média",
        media
    )

with c2:

    st.metric(
        "🏆 Pontuação",
        total
    )

with c3:

    st.metric(
        "⭐ Resultado",
        classificacao
    )

st.divider()
# ==========================================================
# BOTÃO SALVAR
# ==========================================================

from utils.avaliacao import salvar_avaliacao

col1, col2 = st.columns([2, 1])

with col1:

    salvar = st.button(
        "💾 SALVAR AVALIAÇÃO",
        use_container_width=True
    )

with col2:

    limpar = st.button(
        "🧹 LIMPAR",
        use_container_width=True
    )

# ==========================================================
# LIMPAR
# ==========================================================

if limpar:

    st.rerun()

# ==========================================================
# SALVAR
# ==========================================================

if salvar:

    try:

        salvar_avaliacao(

            nome,

            velocidade,

            forca,

            resistencia,

            flexibilidade,

            coordenacao,

            equilibrio,

            observacoes

        )

        st.success("✅ Avaliação salva com sucesso!")

        st.balloons()

    except Exception as erro:

        st.error("Erro ao salvar avaliação.")

        st.exception(erro)

# ==========================================================
# RESUMO FINAL
# ==========================================================

st.divider()

st.subheader("📋 Resumo da Avaliação")

c1, c2 = st.columns(2)

with c1:

    st.write(f"**👤 Atleta:** {nome}")

    st.write(f"**📊 Média:** {media}")

    st.write(f"**🏆 Pontuação:** {total}")

with c2:

    st.write(f"**⭐ Classificação:** {classificacao}")

    st.write(f"**⚡ Velocidade:** {velocidade}")

    st.write(f"**💪 Força:** {forca}")

st.divider()

# ==========================================================
# RESULTADOS DOS TESTES
# ==========================================================

st.subheader("📈 Resultados dos Testes")

st.progress(velocidade / 10)

st.caption(f"⚡ Velocidade: {velocidade}/10")

st.progress(forca / 10)

st.caption(f"💪 Força: {forca}/10")

st.progress(resistencia / 10)

st.caption(f"🏃 Resistência: {resistencia}/10")

st.progress(flexibilidade / 10)

st.caption(f"🤸 Flexibilidade: {flexibilidade}/10")

st.progress(coordenacao / 10)

st.caption(f"🧠 Coordenação: {coordenacao}/10")

st.progress(equilibrio / 10)

st.caption(f"⚖️ Equilíbrio: {equilibrio}/10")

# ==========================================================
# OBSERVAÇÕES
# ==========================================================

if observacoes:

    st.divider()

    with st.expander("📝 Observações da Avaliação"):

        st.write(observacoes)

# ==========================================================
# RODAPÉ
# ==========================================================

st.divider()

st.caption(
    "🏆 SportAvalia PRO V2 • Avaliação Física • Professor Dinaldo Guedes • IFPB"
)