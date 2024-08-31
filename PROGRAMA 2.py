# Crear una matriz bidimensional de 3x3
matriz_original = [[3, 1, 2],
                   [4, 5, 6],
                   [7, 8, 9]]

print("Matriz original:")
for fila in matriz_original:
    print(fila)

# Función para ordenar una fila de la matriz utilizando Bubble Sort
def ordenar_fila(matriz, fila_idx):
    fila = matriz[fila_idx]
    n = len(fila)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Ordenar la fila 0 de la matriz
fila_idx = 0
matriz_ordenada = matriz_original.copy()
matriz_ordenada[fila_idx] = ordenar_fila(matriz_ordenada, fila_idx)

print("\nMatriz con la fila {} ordenada:".format(fila_idx))
for fila in matriz_ordenada:
    print(fila)