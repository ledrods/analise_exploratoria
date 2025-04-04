import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Configuração inicial
st.set_page_config(page_title="Previsão de Preços de Celulares", layout="wide")

# Sidebar de Navegação
st.sidebar.title("Navegação")
st.sidebar.markdown("Selecione uma página acima para explorar o projeto.")

# Título Principal
st.title("📱 Previsão de Preços de Celulares")
st.write("Bem-vindo ao aplicativo interativo para análise e previsão de preços de celulares.")
st.markdown("Navegue pelas abas na barra lateral para ver a análise exploratória, entender a escolha do modelo e testar a previsão.")

# --- 🖼️ IMAGEM RESUMO DO PROJETO ---
st.subheader("📌 Resumo Visual do Projeto")
image_path = "reports/resumo.png"

with st.spinner("📷 Carregando imagem..."):
    try:
        image = Image.open(image_path)
        st.image(image, caption="📊 Infográfico com os Principais Insights do Projeto", use_container_width=True)
    except Exception as e:
        st.warning(f"⚠️ Não foi possível carregar a imagem. Erro: {e}")
