import streamlit as st
from utils import taylorAproximacao as ta
import inspect

def mostrar():
    st.markdown("## Expansão de Taylor para $f(x) = x^m$")
    st.write("Nesta seção analisamos a expansão de Taylor de primeira ordem e a estimativa de erro da segunda ordem da função $f(x) = x^m$.")

    x = st.number_input("Escolha o valor de x", value=2)
    h = st.number_input("Escolha o valor de h", value=1)

    st.latex(r"""
    f(x) = f(x - h) + f'(x - h)h + \frac{f''(x - h)}{2!} h^2 + \cdots
    """)

    df = ta.calcular_taylor(x, h)
    st.write("### Resultados das aproximações:")
    st.dataframe(df, hide_index=True)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar tabela como CSV",
        data=csv,
        file_name="aproximacao_taylor.csv",
        mime='text/csv'
    )


    st.markdown("""
    O termo de erro de segunda ordem fornece uma estimativa de quanto a aproximação de primeira ordem pode se afastar do valor real.  
    Conforme esperado, para \( m = 1 \), a aproximação é exata, e conforme \( m \) aumenta, o erro também cresce.
    """)

    st.write("### Código fonte:")
    source_code = inspect.getsource(ta.calcular_taylor)
    st.code(source_code, language="python")
    st.download_button(
        label="📥 Baixar código-fonte (Aproximação de Taylor)",
        data=source_code,
        file_name="aproximacaoDeTaylor.py",
        mime='text/plain'
    )
