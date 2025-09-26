def bissecao(funcao, a, b, max_iter=10):
    listA = []
    listB = []
    listX = []
    listResult = []

    for i in range(max_iter):
        valor_b = funcao(b)
        x_atual = (a + b) / 2
        listA.append(a)
        listB.append(b)
        listX.append(x_atual)
        listResult.append(funcao(x_atual))
        if funcao(x_atual) == 0:
            return x_atual
        if funcao(x_atual) * valor_b < 0:
            a = x_atual
        else:
            b = x_atual

    return {
        "listA": listA,
        "listB": listB,
        "listX": listX,
        "listResult": listResult
    }

def falsa_posicao(funcao, a, b, max_iter=10):
    listA = []
    listB = []
    listX = []
    listResult = []

    for i in range(max_iter):
        valor_b = funcao(b)
        valor_a = funcao(a)
        x_atual = b - (valor_b * (b - a)) / (valor_b - valor_a)
        listA.append(a)
        listB.append(b)
        listX.append(x_atual)
        listResult.append(funcao(x_atual))
        if funcao(x_atual) == 0:
            return x_atual
        if funcao(x_atual) * valor_a < 0:
            b = x_atual
        else:
            a = x_atual

    return {
        "listA": listA,
        "listB": listB,
        "listX": listX,
        "listResult": listResult
    }
