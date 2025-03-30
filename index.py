import streamlit as st
import calcularMatriz as cm
import analiseDeVibracaoLisas as avl
import pandas as pd
import inspect

st.title("Métodos Numéricos")
st.write("Essa página tem como objetivo apresentar os códigos construidos no projeto de PIBIC de Métodos Numéricos da UnDF.")

st.write("## Biblioteca de códigos:")
st.write("A ideia do projeto é criar uma biblioteca de códigos em Python para Métodos Numéricos. A biblioteca será construída ao longo do projeto com diversos códigos. A seguir, temos a lista de códigos disponíveis:")
st.markdown("""
1. [Calculadora de Determinante de Matriz (Cofator)](#calculadora-de-determinante-de-matriz-cofator)
2. [Análise de vibração (Métodos Numéricos para Engenharia, Quinta Edição p. 170)](#6297aac5)
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

st.write("## Análise de vibração")
st.write("A ideia do código é resolver o estudo de caso do livro **'Métodos Numéricos para Engenharia, Quinta Edição'**. O estudo de caso é sobre a análise de vibração de um sistema de um grau de liberdade.")
st.write("O livro faz uma análise por partes do sistema, adicionando um pouco de dificuldade a cada etapa.")
st.write("### Etapa 1: Aplicando em estradas lisas, achando a constante da mola")
st.write("O código utiliza o método da bisseção para encontrar a constante da mola.")
source_code = inspect.getsource(avl)
st.write("Código fonte da calculadora de determinante de matriz:")
st.code(source_code, language="python")
st.write("#### Explicando o código:")
st.markdown(r"""
Aqui utilizamos essa equação:  

$$
x(t) = \cos(0.05\mu) + \frac{\lambda}{\mu} \cdot \sin(0.05\mu)  
$$  

Abrindo essa equação com as fórmulas:  

$$
\mu = \frac{\sqrt{|c^2 - 4mk|}}{2m}
$$

e

$$
\lambda = \frac{c}{2m}
$$

Temos:

$$
x(t) = \cos\left(0.05 \cdot \sqrt{\frac{k}{m} - \frac{c^2}{4m^2}}\right) + \frac{c}{\sqrt{4km - c^2}} \cdot \sin\left(0.05 \cdot \sqrt{\frac{k}{m} - \frac{c^2}{4m^2}}\right)
$$

Como queremos que o primeiro momento de equilíbrio ocorra em \( t = 0.05 \) e sabemos que \( x \) é a distância da posição de equilíbrio da mola (deve ser zero em \( t = 0.05 \)), podemos igualar a equação a zero e, com as informações passadas no estudo de caso, procurar um \( k \) que satisfaça essa equação.

##### Achando o \( k \):
Para achar o \( k \), optamos por utilizar o método da bisseção, assim como o livro. Optamos por esse método no código por sua similaridade com o método de busca binária. Para começar o método da bisseção, escolhemos \( k_1 \) e \( k_2 \) tais que, se \( k_1 \) aplicado na equação resulta em um número positivo, então \( k_2 \) deve resultar em um negativo.  

O livro propõe dois valores iniciais para \( k_1 \) e \( k_2 \). Através do esboço de um gráfico da equação, é possível aproximar uma opção de valor com um resultado maior e outro menor que 0.  

Após a seleção dos dois valores, podemos simplesmente fazer iterações e calcular o resultado usando:

$$
k = \frac{k_1 + k_2}{2}
$$

O código calcula o resultado para esse \( k \) e substitui o \( k_1 \) ou \( k_2 \) de acordo com o resultado. Dessa forma, podemos aproximar um valor de \( k \) que zere a equação.
""")

st.pyplot(avl.getGraph())
st.pyplot(avl.getGraphEvoK())
st.write("""Ao observar os gráficos podemos notar como o método na bissetriz auxiliou na resolução do problema. 
         Conseguimos ver que o próximo resultado sempre está entre os dois últimos""")