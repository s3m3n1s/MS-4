with open('input.txt', 'r') as f:
    x, p = f.readlines()
    x = [int(xi) for xi in x.split()]
    p = [float(pi) for pi in p.split()]


def matpred(x, p):
    M = 0
    for i in range(len(x)):
        M += x[i] * p[i]
    return M


def dispersion(x, p):
    D = matpred([xi ** 2 for xi in x], p) - matpred(x, p) ** 2
    return D


def meansq(x, p):
    MS = dispersion(x, p) ** 0.5
    return MS


print(f'Матожидание {matpred(x, p)}\nДисперсия {dispersion(x, p)}\nСреднеквадратичное отклонение {meansq(x, p)}')
