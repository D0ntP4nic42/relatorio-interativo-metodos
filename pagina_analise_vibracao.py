import streamlit as st
import pandas as pd
import inspect
from utils.analiseDeVibracaoLisas import AnaliseDeVibracaoLisas
from utils import analiseDeVibracaoRugosas as avr
from utils import metodos

def mostrar():
    avl = AnaliseDeVibracaoLisas()

    st.write("## Análise de vibração")
    st.write("A ideia do código é resolver o estudo de caso do livro **'Métodos Numéricos para Engenharia, Quinta Edição'**. O estudo de caso consiste em encontrar as variáveis que satisfazem a equação da mola de fomra que o carro estabilize de fomra aceitável.")
    st.write("O livro traz a análise em duas etapas. A mais simples leva em consideração estradas lisas, com ela, conseguimos obter *k* que seria a constante da mola. Tendo o valor de *k*, podemos aplicar a segunda etapa, que leva em consideração estradas rugosas. Nessa etapa, conseguimos encontrar o valor de *ωp*, que é a razão entre a frequência de excitação e a frequência natural.")
    st.write("### Etapa 1: Aplicando em estradas lisas, achando a constante da mola")

    source_code = inspect.getsource(AnaliseDeVibracaoLisas)
    st.code(source_code, language="python")
    st.download_button(
        label="📥 Baixar código-fonte (Lisas)",
        data=source_code,
        file_name="analiseDeVibracaoLisas.py",
        mime='text/plain'
    )

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
    """)

    st.write("##### Achando o **\( k \)**:")
    metodo = st.selectbox("Selecione o método numérico utilizado para encontrar o valor de **\( k \)**:", ("Bisseção", "Falsa Posição"), index=1, key="metodo_k")
    avl.metodo = metodo
    avl.calcular()

    if metodo == "Bisseção":
        st.markdown(r"""
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
        st.pyplot(avl.getGrafico())
        st.pyplot(avl.getGraficoEvoK())
        st.write("""Ao observar os gráficos podemos notar como o método na bissetriz auxiliou na resolução do problema. 
                Conseguimos ver que o próximo resultado sempre está entre os dois últimos""")
        st.write("#### Código fonte do método da bisseção utilizado:")
        source_code = inspect.getsource(metodos.bissecao)
        st.code(source_code, language="python")
        st.download_button(
            label="📥 Baixar código-fonte (Bisseção)",
            data=source_code,
            file_name="bissecao.py",
            mime='text/plain'
        )
        st.write("#### Tabela de iterações do método da bisseção:")
        st.dataframe(avl.dataframe, hide_index=True)
    elif metodo == "Falsa Posição":
        st.markdown(r"""
            Para achar o **\( k \)**, optamos por utilizar o método da falsa posição. Esse método é similar ao método da bisseção, mas ao invés de escolher o ponto médio entre os dois últimos valores, escolhemos o ponto onde a reta que liga os dois pontos cruza o eixo x.  

            A cada iteração escolhemos como *k* esse ponto de cruzamento e cálculamos o resultado da equação que queremos achar a raiz.  

            Se o resultado for positivo, substituímos o *k* anterior que resultou em positivo, caso contrário, substituímos o *k* que resultou em negativo.  

            Dessa forma, vamos refinando o valor de *k* até encontrar um valor que zere a equação ou pelo menos uma aproximação com erro aceitável.
                        
            O livro propõe dois valores iniciais para **\( k _1\)** e **\( k _2\)**. Através do esboço de um gráfico da equação, é possível aproximar uma opção de valor com um resultado maior e outro menor que 0.  

            Após a seleção dos dois valores, podemos simplesmente fazer iterações e calcular o resultado usando:

            $$
            k = k_2 - \frac{f(k_2) \cdot (k_2 - k_1)}{f(k_2) - f(k_1)}
            $$

            O código calcula o resultado para esse **\( k \)** e substitui o **\( k _1\)** ou **\( k _2\)** de acordo com o resultado. Dessa forma, podemos aproximar um valor de **\( k \)** que zere a equação.
        """)

        st.pyplot(avl.getGrafico())
        st.pyplot(avl.getGraficoEvoK())
        st.write("Ao observar os gráficos podemos notar como o método da falsa posição auxiliou na resolução do problema.")
        st.write("#### Código fonte do método da falsa posição utilizado:")
        source_code = inspect.getsource(metodos.falsa_posicao)
        st.code(source_code, language="python")
        st.download_button(
            label="📥 Baixar código-fonte (Falsa Posição)",
            data=source_code,
            file_name="falsaPosicao.py",
            mime='text/plain'
        )
        st.write("#### Tabela de iterações do método da falsa posição:")
        st.dataframe(avl.dataframe, hide_index=True)

    csv = avl.dataframe.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar tabela como CSV",
        data=csv,
        file_name=f"k_por_iteracao_{metodo.lower()}.csv",
        mime='text/csv'
    )
    st.write(f"Observe que na tabela conseguimos ver os valores de **\( k _1\)**, **\( k _2\)**, **\( k \)** e o resultado da equação para cada iteração do método numérico utilizado.")

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

    Utilizamos o **método da bisseção** para encontrar o valor de $\omega_p$ que zera essa equação, observe que para acharmos $\zeta precisamos do **\(k\)**.
    """, unsafe_allow_html=True)

    st.write("Código fonte da análise de vibração em estradas rugosas:")
    source_code = inspect.getsource(avr)
    st.code(source_code, language="python")
    st.download_button(
        label="📥 Baixar código-fonte (Rugosas)",
        data=source_code,
        file_name="analiseVibracaoRugosas.py",
        mime='text/plain'
    )

    st.write("#### Tabela de iterações do método da bisseção:")
    st.dataframe(avr.dataFrame, hide_index=True)

    csv = avr.dataFrame.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar tabela como CSV",
        data=csv,
        file_name="omega_p_por_iteracao.csv",
        mime='text/csv'
    )

    st.markdown("#### Gráfico da função $f(\\omega_p)$:", unsafe_allow_html=True)
    st.pyplot(avr.getGrafico())

    st.markdown("#### Evolução do valor de $\\omega_p$ ao longo das iterações:", unsafe_allow_html=True)
    st.pyplot(avr.getGraficoEvoK())

    st.markdown(r"""
    Observando os gráficos, podemos ver o comportamento da função $f(\omega_p)$ e como o método da bisseção vai refinando o valor de $\omega_p$ até atingir a condição de equilíbrio (valor próximo de zero) assim como vimos ocorrer na primeira etapa.
    """, unsafe_allow_html=True)

    st.write("#### Gráfico da posição do carro ao longo do tempo:")
    posicao_inicial = st.slider("Posição inicial do carro (em metros)", min_value=0.0, max_value=1.0, value=0.5, step=0.1, key="posicao_inicial")
    st.pyplot(avr.getGraficoXt(posicaoInicial=posicao_inicial))
    st.write("""Após acharmos o valor de $\omega_p$ e **\(k\)**, podemos calcular a posição do carro ao longo do tempo utilizando a equação da posição da mola em relação ao tempo, considerando o amortecimento e a frequência de excitação.
            Observe que o ponto em que o sistema entra em equilíbrio pela primeira vez é em t = 0.05 assim como solicitado. Observe também que o gráfico corresponde muito bem ao esperado de um sistema subamortecido, onde a posição do carro oscila em torno de um valor de equilíbrio antes de se estabilizar.""")
    