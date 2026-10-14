def ler_matriz(nome_matriz):
    
    print(f"\n--- Definindo a Matriz {nome_matriz} ---")
    while True:
        try:
            linhas = int(input(f"Digite o número de LINHAS da Matriz {nome_matriz}: "))
            colunas = int(input(f"Digite o número de COLUNAS da Matriz {nome_matriz}: "))
            if linhas > 0 and colunas > 0:
                break
            else:
                print("As dimensões devem ser números inteiros positivos.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    matriz = []
    print(f"Digite os elementos da Matriz {nome_matriz} ({linhas}x{colunas}):")
    
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            while True:
                try:
                    elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
                    linha.append(elemento)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        matriz.append(linha)
    
    return matriz, linhas, colunas

def imprimir_matriz(matriz, nome_matriz):
    
    if not matriz:
        print(f"Matriz {nome_matriz} está vazia.")
        return
        
    print(f"\n--- Matriz {nome_matriz} ---")
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:8.2f}", end=" ")
        print()

def multiplicar_matrizes(L, linhas_L, colunas_L, U, linhas_U, colunas_U):
    
    if colunas_L != linhas_U:
        print("\nErro: A multiplicação não é possível.")
        print(f"O número de colunas da Matriz L ({colunas_L}) não é igual ao número de linhas da Matriz U ({linhas_U}).")
        return None

    A = [[0 for _ in range(colunas_U)] for _ in range(linhas_L)]

    for i in range(linhas_L):
        for j in range(colunas_U):
            soma = 0
            for k in range(colunas_L):
                soma += L[i][k] * U[k][j]
            A[i][j] = soma
            
    return A

if __name__ == "__main__":
    # Ler 1º Matriz
    L, linhas_L, colunas_L = ler_matriz("L")
    imprimir_matriz(L, "L")

    # Ler 2º Matriz
    U, linhas_U, colunas_U = ler_matriz("U")
    imprimir_matriz(U, "U")

    # Calcular e imprimir a Matriz Resultante
    print("\nCalculando A = L x U...")
    A = multiplicar_matrizes(L, linhas_L, colunas_L, U, linhas_U, colunas_U)

    if A:
        imprimir_matriz(A, "(Resultado)")