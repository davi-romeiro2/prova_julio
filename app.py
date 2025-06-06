import streamlit as st
import pandas as pd

# Título da aplicação
st.title('Aplicação Básica com Streamlit')

# Texto explicativo
st.write('Faça o upload de um arquivo CSV para visualizar os dados.')

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Carregar os dados do CSV
    df = pd.read_csv(uploaded_file)

    # Exibir as primeiras linhas do dataset
    st.write(df.head())

    # Gráfico ou outra análise
    st.write("Gráfico exemplo:")
    st.bar_chart(df)
