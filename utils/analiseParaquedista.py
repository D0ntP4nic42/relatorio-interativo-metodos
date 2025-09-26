from utils import metodos
import math as math
import pandas as pd
import matplotlib.pyplot as plt

class AnaliseParaquedista:
    num_iteracoes = 60

    g = 9.8
    m = 68.1
    c = 12.5
    listT = []
    listResult = []

    def calcular(self):
        self.listT = []
        self.listResult = []
        t_anterior = 0

        for t in range(0, self.num_iteracoes):
            resultado = self.getResult(t_anterior) + (self.g - self.c / self.m * self.getResult(t_anterior)) * (t - t_anterior)
            self.listT.append(t)
            self.listResult.append(resultado)
            t_anterior = t

        return pd.DataFrame({
            't': self.listT,
            'Resultado': self.listResult
        })

    def getResult(self, t):
        return self.g * self.m / self.c * (1 - math.exp(-self.c / self.m * t))
    
    def getGrafico(self):
        plt.figure(figsize=(8, 5))
        plt.plot(range(len(self.listT)),
                 self.listResult,
                 marker='o', linestyle='-', color='red', label='Velocidade do paraquedista (m/s)')
        plt.xlabel('Iteração')
        plt.ylabel('Velocidade (m/s)')
        plt.title('Evolução da Velocidade do Paraquedista por Iteração')
        plt.grid()
        plt.legend()
        return plt.gcf()