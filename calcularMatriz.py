def expansaoCofatores(matriz):
    for linha in matriz:
        if len(linha) != len(matriz):
            raise ValueError("Matriz não é quadrada")
    
    det = 0
    if len(matriz) == 2:
        det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        return det

    for i in range(len(matriz[0])):
        matrizDoCofator = []
        matrizDoCofator.extend([[] for _ in range(len(matriz) - 1)])
        for j in range(1, len(matriz)):
            for k in range(len(matriz[j])):
                if k == i:
                    continue
                matrizDoCofator[j-1].append(matriz[j][k])
        det += matriz[0][i] * (-1)**(i + 2) * expansaoCofatores(matrizDoCofator)
    return det