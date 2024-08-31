# Crear una matriz bidimensional de 3x3
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Función para buscar un valor en la matriz
def buscar_valor_en_matriz(matriz, valor_buscar):
    for fila_idx, fila in enumerate(matriz):
        for col_idx, valor in enumerate(fila):
            if valor == valor_buscar:
                print(f"Valor {valor_buscar} encontrado en la posición ({fila_idx}, {col_idx})")
                return (fila_idx, col_idx)
    print(f"Valor {valor_buscar} no encontrado en la matriz")
    return None

# Buscar un valor en la matriz
valor_buscar = 10
resultado = buscar_valor_en_matriz(matriz, valor_buscar)

if resultado:
    print(f"Posición del valor {valor_buscar}: {resultado}")
else:
    print(f"Valor {valor_buscar} no encontrado")
