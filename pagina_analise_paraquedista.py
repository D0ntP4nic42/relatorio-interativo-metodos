import streamlit as st
import pandas as pd
import inspect
from utils.analiseParaquedista import AnaliseParaquedista

def mostrar():
    ap = AnaliseParaquedista()
    st.write("## Análise do Paraquedista")
    st.write("A ideia do código é resolver o estudo de caso do livro **'Métodos Numéricos para Engenharia, Quinta Edição'**. O estudo de caso consiste em encontrar a velocidade máxima que um paraquedista chegará em queda livre.")
    st.write("O livro traz a análise de forma numérica e analítica, o código implementa o método numérico de Euler para resolver o problema utilizando a mesma equação encontrada no livro para a forma numérica da solução.")
    st.write("### Equação diferencial do movimento do paraquedista")
    st.latex(r"""
        \begin{equation}
            v(t) = \frac{g \cdot m}{c} \left( 1 - e^{-\frac{c}{m} t} \right)
        \end{equation}
    """)
    st.write("Onde:")
    st.latex(r"""
        \begin{equation}
            \begin{aligned}
                v(t) & : \text{velocidade do paraquedista em função do tempo (m/s)} \\
                g & : \text{aceleração da gravidade (m/s}^2\text{) = 9.8} \\
                m & : \text{massa do paraquedista (kg) = 68.1} \\
                c & : \text{coeficiente de resistência do ar (kg/s) = 12.5} \\
                t & : \text{tempo de queda (s)}
            \end{aligned}
        \end{equation}
    """)
    st.write("Para esse problema possuímos valores fixados e aplicamos eles no método de Euler. Antes disso, é possível realizar o cálculo analítico da velocidade terminal do paraquedista, que é o valor que a velocidade tende a se estabilizar com o passar do tempo aplicando os valores dados.")

    st.latex(r"""
        \begin{equation}
            v(t) = \frac{9.8 \cdot 68.1}{12.5} \left( 1 - e^{-\frac{12.5}{68.1} t} \right)
        \end{equation}
    """)
    st.latex(r"""
        \begin{equation}
            v(t) = 53.38 \left( 1 - e^{-0.1835 t} \right)
        \end{equation}
    """)
    st.write("Com isso, podemos calcular a velocidade terminal do paraquedista, que é o valor que a velocidade tende a se estabilizar com o passar do tempo. Em muitos casos a solução analítica é difícil de ser encontrada, por isso o método numérico é uma alternativa viável para encontrar a solução aproximada.")
    st.write("### Utilizando o método de Euler")
    st.write("Aqui utilizaremos o método sugerido pelo livro, precisamos também modificar nossa equação de forma que considere a variação da velocidade em relação ao tempo, ou seja, a derivada da velocidade em relação ao tempo.")
    st.latex(r"""
        \begin{equation}
            \frac{v(t_i+1) - v(t_i)}{t_{i+1} - t_i} = \frac{g \cdot m}{c} e^{-\frac{c}{m} t_1}
        \end{equation}
    """)
    st.write("Isolando a variável independente, temos:")
    st.latex(r"""
        \begin{equation}
            v(t_{i+1}) = v(t_i) + \frac{g \cdot m}{c} e^{-\frac{c}{m} t_i} (t_{i+1} - t_i)
        \end{equation}
    """)
    st.write("Com isso, podemos aplicar o método de Euler para encontrar a velocidade do paraquedista em cada instante de tempo. O código implementa o método de Euler para calcular a velocidade do paraquedista.")
    st.number_input("Número de iterações (Coloque valores próximos de 30 para um resultado mais preciso)", min_value=2, max_value=1000, value=60, step=1, key="iteracoes_paraquedista")
    ap.num_iteracoes = st.session_state.iteracoes_paraquedista
    st.dataframe(ap.calcular(), hide_index=True)
    st.pyplot(ap.getGrafico())
    st.write("Código fonte da análise do paraquedista:")
    source_code = inspect.getsource(AnaliseParaquedista)
    st.code(source_code, language="python")
    st.download_button(
        label="📥 Baixar código-fonte (Análise do Paraquedista)",
        data=source_code,
        file_name="analiseParaquedista.py",
        mime='text/plain'
    )
