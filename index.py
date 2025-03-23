import streamlit as st
import calcularMatriz as cm
import pandas as pd
import inspect

st.title("Métodos Numéricos")
st.write("Essa página tem como objetivo apresentar os códigos construidos no projeto de PIBIC de Métodos Numéricos da UnDF.")

st.write("## Biblioteca de códigos:")
st.write("A ideia do projeto é criar uma biblioteca de códigos em Python para Métodos Numéricos. A biblioteca será construída ao longo do projeto com diversos códigos. A seguir, temos a lista de códigos disponíveis:")
st.markdown("""
1. [Calculadora de Determinante de Matriz (Cofator)](#calculadora-de-determinante-de-matriz-cofator)
2. [Outro Código Futuro](#outro-codigo-futuro)
""", unsafe_allow_html=True)

st.write("## Calculadora de determinante de matriz (Cofator)")
st.write("A calculadora de determinante de matriz é um código que calcula o determinante de uma matriz quadrada de qualquer ordem. O código utiliza o método de cofatores para realizar o cálculo.")

ordem = 2

st.write("Digite a ordem da matriz:")
ordem = st.text_input("Ordem da matriz:", ordem)
ordem = int(ordem)

qtdColunas = ordem
qtdLinhas = ordem

data = pd.DataFrame([[0] * qtdColunas for _ in range(qtdLinhas)])

matriz = st.data_editor(
    data,
    hide_index=True,
)

if st.button("Calcular determinante"):
    determinante = cm.expansaoCofatores(matriz.values)
    st.write("O determinante da matriz é: ", determinante)

st.write("### Utilizando a função: ")

with st.echo():
    import calcularMatriz as cm
    determinante = cm.expansaoCofatores(matriz.values)
    st.write("O determinante da matriz é: ", determinante)

source_code = inspect.getsource(cm.expansaoCofatores)
st.write("Código fonte da calculadora de determinante de matriz:")
st.code(source_code, language="python")