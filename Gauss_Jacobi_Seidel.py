import numpy as np

def gauss_jacobi(A, b, x0, tol, max_iter):
   
    n = len(b)
    x = x0.copy() 
    x_novo = np.zeros_like(x) 
    
    print(f"--- Iniciando Método de Gauss-Jacobi ---")
    print(f"x(0) = {x.ravel()}")

    for k in range(max_iter):
        
        for i in range(n):
            
            soma = 0
            for j in range(n):
                if i != j:
                    soma += A[i, j] * x[j]
            
            x_novo[i] = (b[i] - soma) / A[i, i]

        numerador = np.linalg.norm(x_novo - x, np.inf)
        denominador = np.linalg.norm(x_novo, np.inf)
        
        if denominador == 0:
            Dr = 0.0
        else:
            Dr = numerador / denominador

        x = x_novo.copy()

        print(f"Iteração {k+1}: x = {np.round(x.ravel(), 5)}, Dr = {Dr:.2e}")

        if Dr < tol:
            print(f"\nConvergência alcançada em {k+1} iterações.")
            return x, k + 1
            
    print(f"\nMétodo não convergiu após {max_iter} iterações.")
    return x, max_iter

def gauss_seidel(A, b, x0, tol, max_iter):
    
    n = len(b)
    x = x0.copy() 
    print(f"\n--- Iniciando Método de Gauss-Seidel ---")
    print(f"x(0) = {x.ravel()}")
    
    for k in range(max_iter):
        x_anterior = x.copy() 

        for i in range(n):
            
            soma_novos = 0
            for j in range(i):
                soma_novos += A[i, j] * x[j] 
            
            soma_antigos = 0
            for j in range(i + 1, n):
            
                soma_antigos += A[i, j] * x_anterior[j] 

            x[i] = (b[i] - soma_novos - soma_antigos) / A[i, i]

        numerador = np.linalg.norm(x - x_anterior, np.inf)
        denominador = np.linalg.norm(x, np.inf)

        if denominador == 0:
            Dr = 0.0
        else:
            Dr = numerador / denominador
            
        print(f"Iteração {k+1}: x = {np.round(x.ravel(), 5)}, Dr = {Dr:.2e}")

        if Dr < tol:
            print(f"\nConvergência alcançada em {k+1} iterações.")
            return x, k + 1
            
    print(f"\nMétodo não convergiu após {max_iter} iterações.")
    return x, max_iter


if __name__ == "__main__":
    
    A = np.array([[2.0, -1.0, 0.0],
                  [-1.0, 3.0, -1.0],
                  [0.0, -1.0, 2.0]])
    
    b = np.array([1.0, 8.0, -5.0])
    
    # Aproximação inicial x(0)
    x0 = np.array([0.0, 0.0, 0.0])
    
    # Tolerância
    tolerancia = 1e-5
    
    # Número máximo de iterações para evitar loops infinitos
    max_iteracoes = 50

    # Resolvendo com Gauss-Jacobi
    solucao_jacobi, iter_jacobi = gauss_jacobi(A, b, x0, tolerancia, max_iteracoes)
    print(f"Solução final (Jacobi): {solucao_jacobi}")
    print(f"Total de iterações (Jacobi): {iter_jacobi}")

    print("\n" + "="*30 + "\n")

    # Resolvendo com Gauss-Seidel
    solucao_seidel, iter_seidel = gauss_seidel(A, b, x0, tolerancia, max_iteracoes)
    print(f"Solução final (Seidel): {solucao_seidel}")
    print(f"Total de iterações (Seidel): {iter_seidel}")