# ==========================================================
# SPORTAVALIA PRO V2
# ATLETAS.PY
# PARTE 1
# ==========================================================

import streamlit as st

from pathlib import Path

from utils.excel import (
    listar_dados_atletas,
    pesquisar_atletas,
    excluir_atleta
)
# Espaço após configurar a página
st.write("")
st.write("")
st.write("")

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

st.set_page_config(
    page_title="Atletas",
    page_icon="🏃",
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
# CABEÇALHO
# ==========================================================

st.title("🏃 Atletas")

st.caption("SportAvalia PRO V2")

st.divider()

# ==========================================================
# CARREGAR DADOS
# ==========================================================

try:

    atletas = listar_dados_atletas()

except Exception as erro:

    st.error("Erro ao carregar atletas.")

    st.exception(erro)

    st.stop()

# ==========================================================
# INDICADORES
# ==========================================================

c1, c2, c3 = st.columns([3, 1, 1])

with c1:

    pesquisa = st.text_input(
        "🔎 Pesquisar atleta"
    )

with c2:

    st.metric(
        "👥 Total",
        len(atletas)
    )

with c3:

    st.metric(
        "🏆 Esportes",
        len(
            set(
                [
                    a.get("esporte", "")
                    for a in atletas
                ]
            )
        )
    )

# ==========================================================
# PESQUISA
# ==========================================================

if pesquisa.strip():

    atletas = pesquisar_atletas(
        pesquisa
    )

# ==========================================================
# SEM RESULTADOS
# ==========================================================

if len(atletas) == 0:

    st.warning(
        "Nenhum atleta encontrado."
    )

    st.stop()

# ==========================================================
# LISTA
# ==========================================================

st.divider()

st.subheader(
    "📋 Atletas cadastrados"
)

st.write(
    f"Encontrados **{len(atletas)}** atleta(s)."
)
# ==========================================================
# CARDS DOS ATLETAS
# ==========================================================

for atleta in atletas:

    nome = atleta.get("nome", "")

    sexo = atleta.get("sexo", "")

    idade = atleta.get("idade", "")

    esporte = atleta.get("esporte", "")

    equipe = atleta.get("equipe", "")

    treinador = atleta.get("treinador", "")

    altura = atleta.get("altura", "")

    peso = atleta.get("peso", "")

    imc = atleta.get("imc", "")

    telefone = atleta.get("telefone", "")

    email = atleta.get("email", "")

    observacoes = atleta.get("observacoes", "")

    with st.container(border=True):

        c1, c2 = st.columns([1,5])

        # =====================================
        # AVATAR
        # =====================================

        with c1:

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

        # =====================================
        # DADOS
        # =====================================

        with c2:

            st.markdown(f"## 👤 {nome}")

            l1, l2, l3 = st.columns(3)

            with l1:

                st.write(f"**🏆 Esporte:** {esporte}")

                st.write(f"**🎂 Idade:** {idade}")

                st.write(f"**👥 Sexo:** {sexo}")

            with l2:

                st.write(f"**🏟 Equipe:** {equipe}")

                st.write(f"**👨‍🏫 Treinador:** {treinador}")

                st.write(f"**📏 Altura:** {altura}")

            with l3:

                st.write(f"**⚖ Peso:** {peso}")

                st.write(f"**📊 IMC:** {imc}")

                st.write(f"**📱 Telefone:** {telefone}")

            if email:

                st.caption(f"📧 {email}")

            if observacoes:

                with st.expander("📝 Observações"):

                    st.write(observacoes)

        st.divider()

        # =====================================================
        # BOTÕES
        # (Parte 3 continuará daqui)
        # =====================================================
                # =====================================================
        # AÇÕES
        # =====================================================

        b1, b2, b3 = st.columns(3)

        # ---------------------------------
        # ABRIR
        # ---------------------------------

        with b1:

            if st.button(
                "📂 Abrir",
                key=f"abrir_{nome}",
                use_container_width=True
            ):

                st.session_state["atleta_visualizar"] = nome

                st.success(f"{nome} selecionado.")

        # ---------------------------------
        # EDITAR
        # ---------------------------------

        with b2:

            if st.button(
                "✏️ Editar",
                key=f"editar_{nome}",
                use_container_width=True
            ):

                st.session_state["modo"] = "editar"

                st.session_state["atleta_edicao"] = nome

                st.switch_page("pages/Cadastro.py")

        # ---------------------------------
        # EXCLUIR
        # ---------------------------------

        with b3:

            if st.button(
                "🗑️ Excluir",
                key=f"excluir_{nome}",
                use_container_width=True
            ):

                st.session_state["confirmar_exclusao"] = nome

        # =====================================================
        # CONFIRMAÇÃO
        # =====================================================

        if st.session_state.get("confirmar_exclusao") == nome:

            st.warning(
                f"Tem certeza que deseja excluir **{nome}**?"
            )

            c1, c2 = st.columns(2)

            with c1:

                if st.button(
                    "✅ Sim, excluir",
                    key=f"sim_{nome}",
                    use_container_width=True
                ):

                    try:

                        excluir_atleta(nome)

                        st.success(
                            "Atleta excluído com sucesso."
                        )

                        st.session_state.pop(
                            "confirmar_exclusao",
                            None
                        )

                        st.rerun()

                    except Exception as erro:

                        st.error("Erro ao excluir.")

                        st.exception(erro)

            with c2:

                if st.button(
                    "❌ Cancelar",
                    key=f"nao_{nome}",
                    use_container_width=True
                ):

                    st.session_state.pop(
                        "confirmar_exclusao",
                        None
                    )

                    st.rerun()

# ==========================================================
# RODAPÉ
# ==========================================================

st.divider()

st.caption(
    "SportAvalia PRO v2 • Professor Dinaldo Guedes • IFPB"
)