import streamlit as st
import pagina_analise_vibracao
import pagina_determinante
from utils import calcularMatriz as cm
from utils import analiseDeVibracaoLisas as avl
from utils import analiseDeVibracaoRugosas as avr
import pagina_exponencial
import pandas as pd
import inspect


st.title("Métodos Numéricos")
st.write("Essa página tem como objetivo apresentar os códigos construidos no projeto de PIBIC de Métodos Numéricos da UnDF.")

st.write("## Biblioteca de códigos:")
st.write("A ideia do projeto é criar uma biblioteca de códigos em Python para Métodos Numéricos. A biblioteca será construída ao longo do projeto com diversos códigos. A seguir, temos a lista de códigos disponíveis:")

# st.markdown("""
# 1. [Calculadora de Determinante de Matriz (Cofator)](#calculadora-de-determinante-de-matriz-cofator)
# 2. [Análise de vibração (Métodos Numéricos para Engenharia, Quinta Edição p. 170)](#6297aac5)  
#     2.1 [Etapa 1: Aplicando em estradas lisas, achando a constante da mola](#etapa-1-aplicando-em-estradas-lisas-achando-a-constante-da-mola)  
#     2.2 [Etapa 2: Aplicando em estradas rugosas](#etapa-2-aplicando-em-estradas-rugosas)
# 3. [Aproximação com Série de Taylor](#b58cb642)
# """, unsafe_allow_html=True)

pagina = st.sidebar.selectbox("Escolha a página", [
    "Calculadora de Determinante de Matriz (Cofator)",
    "Análise de Vibração",
    "Expansão de Taylor"
])

if pagina == "Análise de Vibração":
    pagina_analise_vibracao.mostrar()
elif pagina == "Expansão de Taylor":
    pagina_exponencial.mostrar()
elif pagina == "Calculadora de Determinante de Matriz (Cofator)":
    pagina_determinante.mostrar()