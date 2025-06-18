import streamlit as st
import pandas as pd
import inspect
from utils import calcularMatriz as cm

def mostrar():
    st.write("## Calculadora de determinante de matriz (Cofator)")
    st.write("A calculadora de determinante de matriz é um código que calcula o determinante de uma matriz quadrada de qualquer ordem. O código utiliza o método de cofatores para realizar o cálculo.")
    st.write("Escolhemos abordar esse método pela simplicidade de implementação em algorítmo.")

    ordem = 2

    st.write("Digite a ordem da matriz:")
    ordem = st.text_input("Ordem da matriz:", ordem)
    try:
        ordem = int(ordem)
    except ValueError:
        st.error("Por favor, insira um número inteiro válido para a ordem da matriz.")
        ordem = 2

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
        determinante = cm.expansaoCofatores(matriz.values)

    st.write("Código fonte da calculadora de determinante de matriz:")
    source_code = inspect.getsource(cm.expansaoCofatores)
    st.code(source_code, language="python")
    st.download_button(
        label="📥 Baixar código-fonte (Determinante)",
        data=source_code,
        file_name="determinante.py",
        mime='text/plain'
    )