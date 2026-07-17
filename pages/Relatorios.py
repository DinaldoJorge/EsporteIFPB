import streamlit as st
from pathlib import Path
from utils.excel import listar_atletas, ler_cadastro
from utils.relatorios import gerar_pdf, obter_pdf

# Espaço após configurar a página
st.write("")
st.write("")
st.write("")
st.set_page_config(page_title="Relatórios",page_icon="📄",layout="wide")

css=Path("styles.css")
if css.exists():
    st.markdown(f"<style>{css.read_text(encoding='utf-8')}</style>",unsafe_allow_html=True)

st.title("📄 Relatórios SportAvalia PRO")

atletas=listar_atletas()
if not atletas:
    st.warning("Nenhum atleta cadastrado.")
    st.stop()

nome=st.selectbox("Selecione o atleta",atletas)
dados=ler_cadastro(nome)

c1,c2=st.columns([2,1])
with c1:
    st.subheader("Dados do Atleta")
    st.write(f"**Nome:** {dados['nome']}")
    st.write(f"**Esporte:** {dados['esporte']}")
    st.write(f"**Equipe:** {dados['equipe']}")
    st.write(f"**Treinador:** {dados['treinador']}")
with c2:
    st.metric("Idade",dados['idade'])
    st.metric("IMC",dados['imc'])

st.divider()

if st.button("📄 Gerar Relatório PDF",use_container_width=True):
    pdf=gerar_pdf(nome)
    st.success("Relatório gerado com sucesso!")

pdf=obter_pdf(nome)
if pdf:
    with open(pdf,"rb") as f:
        st.download_button("⬇️ Baixar PDF",f,file_name=Path(pdf).name,use_container_width=True)
