import streamlit as st
import calcularMatriz as cm
import analiseDeVibracaoLisas as avl
import analiseDeVibracaoRugosas as avr
import pandas as pd
import inspect

st.title("Métodos Numéricos")
st.write("Essa página tem como objetivo apresentar os códigos construidos no projeto de PIBIC de Métodos Numéricos da UnDF.")

st.write("## Biblioteca de códigos:")
st.write("A ideia do projeto é criar uma biblioteca de códigos em Python para Métodos Numéricos. A biblioteca será construída ao longo do projeto com diversos códigos. A seguir, temos a lista de códigos disponíveis:")
st.markdown("""
1. [Calculadora de Determinante de Matriz (Cofator)](#calculadora-de-determinante-de-matriz-cofator)
2. [Análise de vibração (Métodos Numéricos para Engenharia, Quinta Edição p. 170)](#6297aac5)  
    2.1 [Etapa 1: Aplicando em estradas lisas, achando a constante da mola](#etapa-1-aplicando-em-estradas-lisas-achando-a-constante-da-mola)  
    2.2 [Etapa 2: Aplicando em estradas rugosas](#etapa-2-aplicando-em-estradas-rugosas)
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

st.write("Código fonte da calculadora de determinante de matriz:")
source_code = inspect.getsource(cm.expansaoCofatores)
st.code(source_code, language="python")

st.write("## Análise de vibração")
st.write("A ideia do código é resolver o estudo de caso do livro **'Métodos Numéricos para Engenharia, Quinta Edição'**. O estudo de caso consiste em encontrar as variáveis que satisfazem a equação da mola de fomra que o carro estabilize de fomra aceitável.")
st.write("O livro traz a análise em duas etapas. A mais simples leva em consideração estradas lisas, com ela, conseguimos obter *k* que seria a constante da mola. Tendo o valor de *k*, podemos aplicar a segunda etapa, que leva em consideração estradas rugosas. Nessa etapa, conseguimos encontrar o valor de *ωp*, que é a razão entre a frequência de excitação e a frequência natural.")
st.write("### Etapa 1: Aplicando em estradas lisas, achando a constante da mola")
source_code = inspect.getsource(avl)
st.code(source_code, language="python")
st.write("#### Explicando o código:")
st.markdown(r"""
Aqui utilizamos a equação da distância da mola em relação à posição de equilíbrio em função do tempo em sistemas subamortecidos, que é dada por:  

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

Sabendo que **x** precisa ser **igual** a **0** pela primeira vez quando **t = 0,05**, **m = 1.2 x 10^6** g e c = 1 x 10^7 g/s, podemos substituir esses valores na equação e procurar o valor de ****\( k \)****.

##### Achando o **\( k \)**:
Para achar o **\( k \)**, optamos por utilizar o método da bisseção, assim como o livro. Optamos por esse método no código por sua similaridade com o método de busca binária. Para começar o método da bisseção, escolhemos **\( k _1\)** e **\( k _2\)** tais que, se **\( k _1\)** aplicado na equação resulta em um número positivo, então **\( k _2\)** deve resultar em um negativo.  
  
A partir desses valores, fazemos iterações para encontrar um valor de *k* que zere a equação. A cada iteração escolhemos como *k* o ponto médio entre os dois últimos valores e cálculamos o resultado da equação que queremos achar a raiz.  

Se o resultado for positivo, substituímos o *k* anterior que resultou em positivo, caso contrário, substituímos o *k* que resultou em negativo.  

Dessa forma, vamos refinando o valor de *k* até encontrar um valor que zere a equação ou pelo menos uma aproximação com erro aceitável.
            
O livro propõe dois valores iniciais para **\( k _1\)** e **\( k _2\)**. Através do esboço de um gráfico da equação, é possível aproximar uma opção de valor com um resultado maior e outro menor que 0.  

Após a seleção dos dois valores, podemos simplesmente fazer iterações e calcular o resultado usando:

$$
k = \frac{k_1 + k_2}{2}
$$

O código calcula o resultado para esse **\( k \)** e substitui o **\( k _1\)** ou **\( k _2\)** de acordo com o resultado. Dessa forma, podemos aproximar um valor de **\( k \)** que zere a equação.
""")

st.pyplot(avl.getGraph())
st.pyplot(avl.getGraphEvoK())
st.write("""Ao observar os gráficos podemos notar como o método na bissetriz auxiliou na resolução do problema. 
         Conseguimos ver que o próximo resultado sempre está entre os dois últimos""")
st.write("#### Tabela de iterações do método da bisseção:")
st.dataframe(avl.dataframe, hide_index=True)
st.write("Observe que na tabela conseguimos ver os valores de **\( k _1\)**, **\( k _2\)**, **\( k \)** e o resultado da equação para cada iteração do método da bisseção.")

st.write("### Etapa 2: Aplicando em estradas rugosas")
st.write("A segunda parte da análise de vibração considera que o veículo está passando por estradas rugosas.")
st.write("Nessa situação, usamos uma equação diferente, levando em conta a frequência de excitação provocada pelas irregularidades da pista.")

st.write("### Equação utilizada:")
st.latex(r"""
f(\omega_p) = 2 \cdot \sqrt{(1 - \omega_p^2)^2 + 4 \cdot \zeta^2 \cdot \omega_p^2} - 1
""")

st.markdown(r"""
Onde:  
- $\omega_p = \frac{\omega}{\omega_n}$ é a razão entre a frequência de excitação $\omega$ e a frequência natural $\omega_n$.  
- $\zeta = \frac{c}{2 \sqrt{k \cdot m}}$ é o fator de amortecimento crítico.  
- A equação foi igualada a 1 com base nas condições do estudo de caso.  

Utilizamos novamente o **método da bisseção** para encontrar o valor de $\omega_p$ que zera essa equação.
""", unsafe_allow_html=True)


source_code = inspect.getsource(avr)
st.write("Código fonte da análise de vibração em estradas rugosas:")
st.code(source_code, language="python")

st.write("#### Tabela de iterações do método da bisseção:")
st.dataframe(avr.dataFrame, hide_index=True)

st.markdown("#### Gráfico da função $f(\\omega_p)$:", unsafe_allow_html=True)
st.pyplot(avr.getGraph())

st.markdown("#### Evolução do valor de $\\omega_p$ ao longo das iterações:", unsafe_allow_html=True)
st.pyplot(avr.getGraphEvoK())

st.markdown(r"""
Observando os gráficos, podemos ver o comportamento da função $f(\omega_p)$ e como o método da bisseção vai refinando o valor de $\omega_p$ até atingir a condição de equilíbrio (valor próximo de zero).
""", unsafe_allow_html=True)

st.pyplot(avr.getGraphXt())
