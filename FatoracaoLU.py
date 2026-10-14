import numpy as np

def fatoracao_lu(A):
    
    n = A.shape[0]
    U = np.copy(A).astype(float)
    L = np.eye(n, dtype=float)

    contador_iteracoes = 0

    for k in range(n-1):
        for i in range(k+1, n):
            contador_iteracoes += 1
            m = U[i,k] / U[k,k]
            L[i,k] = m
            U[i,k:] = U[i,k:] - m * U[k,k:]
            
    return L, U, contador_iteracoes

def triangular_inferior(L, b):
    
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        soma_produtos = np.dot(L[i, :i], y[:i])
        y[i] = (b[i] - soma_produtos) / L[i, i]
    return y

def triangular_superior(U, y):

    n = len(y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma_produtos = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (y[i] - soma_produtos) / U[i, i]
    return x

A = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
b = np.array([8, 7, 14, -7])

# Passo 1: Fatoração
L, U, iteracoes = fatoracao_lu(A)

print(f"\nA fase de decomposição LU foi concluída em {iteracoes} iterações.\n")
print("Matriz L (Triangular Inferior):")
print(L)
print("\nMatriz U (Triangular Superior):")
print(U)
print("-" * 35)

# Passo 2: Resolver Ly = b
y = triangular_inferior(L, b)
print("Vetor intermediário (y) após resolver Ly = b:")
print(y)
print("-" * 35)

# Passo 3: Resolver Ux = y
solucao_lu = triangular_superior(U, y)
print("Solução (x1, x2, x3, x4) após resolver Ux = y:")
print(solucao_lu)
print("\n" + "="*45 + "\n")