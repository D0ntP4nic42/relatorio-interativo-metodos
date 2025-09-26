import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

m = 1.2 * (10**6)
c = 1 * (10**7)
k_final = 1.397000e+09

fatorDeAmortecimento = c / (2 * math.sqrt(k_final * m))

def getResultOmegaP(omegaP):
    parte1 = (1 - omegaP**2)**2
    parte2 = 4 * (fatorDeAmortecimento**2) * (omegaP**2)
    return 2 * math.sqrt(parte1 +  parte2) - 1

omegaP1 = 0
omegaP2 = 1

listOmegaP1 = []
listOmegaP2 = []
listOmegaP = []
listResultOmegaP = []

for i in range(0, 20):
    omegaP = (omegaP1 + omegaP2) / 2
    result = getResultOmegaP(omegaP)

    listOmegaP1.append(omegaP1)
    listOmegaP2.append(omegaP2)
    listOmegaP.append(omegaP)
    listResultOmegaP.append(result)

    if abs(result) < 1e-6:
        break

    if result < 0:
        omegaP2 = omegaP
    else:
        omegaP1 = omegaP

dataFrame = pd.DataFrame({
    'Omega/P1': listOmegaP1,
    'Omega/P2': listOmegaP2,
    'Omega/P': listOmegaP,
    'Resultado': listResultOmegaP
})

def getGraph():
    omega_range = np.linspace(0, 2, 500)
    values = [getResultOmegaP(w) for w in omega_range]

    plt.figure(figsize=(8, 5))
    plt.plot(omega_range, values, label='f(ωp)')
    plt.axhline(0, color='black', linestyle='--', label='Equilíbrio')
    plt.axvline(listOmegaP[-1], color='red', linestyle='--', label=f'ωp ≈ {listOmegaP[-1]:.4f}')
    plt.xlabel("ωp")
    plt.ylabel("f(ωp)")
    plt.title("Análise em Estradas Rugosas")
    plt.grid()
    plt.legend()
    return plt

def getGraphEvoK():
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(listOmegaP)), listOmegaP, marker='o', linestyle='-', color='green', label='Valor de ωp')
    plt.xlabel("Iteração")
    plt.ylabel("ωp")
    plt.title("Evolução de ωp no Método da Bisseção")
    plt.grid()
    plt.legend()
    return plt

def getGraphXt(posicaoInicial=0.5):
    import numpy as np

    omega_n = math.sqrt(k_final / m)
    zeta = fatorDeAmortecimento
    lambda_ = zeta * omega_n
    mu = omega_n * math.sqrt(1 - zeta**2)

    t = np.linspace(0, 1, 400)

    # Condições iniciais
    x0 = posicaoInicial
    v0 = 0

    A = x0
    B = (v0 + lambda_ * A) / mu

    x_t = np.exp(-lambda_ * t) * (A * np.cos(mu * t) + B * np.sin(mu * t))

    plt.figure(figsize=(8, 5))
    plt.plot(t, x_t, label='x(t)')
    plt.axvline(0.05, color='red', linestyle='--', label='t = 0.05s')
    plt.xlabel("Tempo (s)")
    plt.ylabel("Deslocamento x(t) (m)")
    plt.title("Deslocamento x(t) em Estradas Rugosas")
    plt.grid()
    plt.legend()
    return plt


getGraphXt().show()