import streamlit as st
import pagina_analise_vibracao
import pagina_determinante
import pagina_exponencial
import pagina_analise_paraquedista

st.title("Métodos Numéricos")
st.write("Essa página tem como objetivo apresentar os códigos construidos no projeto de PIBIC de Métodos Numéricos da UnDF.")

st.write("## Biblioteca de códigos:")
st.write("A ideia do projeto é criar uma biblioteca de códigos em Python para Métodos Numéricos. A biblioteca será construída ao longo do projeto com diversos códigos. A seguir, temos a lista de códigos disponíveis:")

pagina = st.sidebar.selectbox("Escolha a página", [
    "Calculadora de Determinante de Matriz (Cofator)",
    "Análise de Vibração",
    "Expansão de Taylor",
    "Análise do Paraquedista"
])

if pagina == "Análise de Vibração":
    pagina_analise_vibracao.mostrar()
elif pagina == "Expansão de Taylor":
    pagina_exponencial.mostrar()
elif pagina == "Calculadora de Determinante de Matriz (Cofator)":
    pagina_determinante.mostrar()
elif pagina == "Análise do Paraquedista":
    pagina_analise_paraquedista.mostrar()