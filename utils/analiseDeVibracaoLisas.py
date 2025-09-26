import math as math
import pandas as pd
import matplotlib.pyplot as plt
from utils import metodos

class AnaliseDeVibracaoLisas:
    def __init__(self, k1=1e9, k2=2e9, metodo="Bisseção"):
        self.k1 = k1
        self.k2 = k2
        self.metodo = metodo
        self.resultadoRaiz = None
        self.dataframe = None

    def getResult(self, k):
        m = 1.2e6
        c = 1e7
        return math.cos(0.05 * math.sqrt((k/m) - c**2/(4*m**2))) + \
               c/(math.sqrt(4*k*m - c**2)) * math.sin(0.05 * math.sqrt(k/m - c**2/(4*m**2)))

    def calcular(self):
        if self.metodo == "Bisseção":
            self.resultadoRaiz = metodos.bissecao(self.getResult, self.k1, self.k2)
        elif self.metodo == "Falsa Posição":
            self.resultadoRaiz = metodos.falsa_posicao(self.getResult, self.k1, self.k2)
        else:
            raise ValueError(f"Método desconhecido: {self.metodo}")

        self.dataframe = pd.DataFrame({
            'K1': self.resultadoRaiz["listA"],
            'K2': self.resultadoRaiz["listB"],
            'K': self.resultadoRaiz["listX"],
            'Resultado': self.resultadoRaiz["listResult"]
        })

    def getGraph(self):
        plt.figure(figsize=(8, 5))
        plt.plot(range(len(self.resultadoRaiz["listX"])),
                 self.resultadoRaiz["listResult"],
                 marker='o', linestyle='-', label='Resultado da equação')
        plt.axhline(0, color='black', linestyle='--', linewidth=0.8, label='Equilíbrio')
        plt.xlabel('Iteração')
        plt.ylabel('Resultado (m)')
        plt.title('Convergência do valor de M')
        plt.legend()
        plt.grid()
        return plt.gcf()

    def getGraphEvoK(self):
        plt.figure(figsize=(8, 5))
        plt.plot(range(len(self.resultadoRaiz["listX"])),
                 self.resultadoRaiz["listX"],
                 marker='o', linestyle='-', color='red', label='Valor de k')
        plt.xlabel('Iteração')
        plt.ylabel('Valor de k (g / s²)')
        plt.title('Evolução do Valor de k por Iteração')
        plt.grid()
        plt.legend()
        return plt.gcf()