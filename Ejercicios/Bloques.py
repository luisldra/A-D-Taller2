import numpy as np
from scipy.sparse import random, csr_matrix

def procesar_bloque(bloque, fila, columna):
    print(f"Procesando bloque en ({fila}, {columna}) con {bloque.nnz} elementos no nulos")

# Parámetros
N = 256  # Tamaño total de la matriz
B = 64   # Tamaño de bloque
density = 0.01

# Crear matriz dispersa
matriz = random(N, N, density=density, format='csr')

# Procesar por bloques
for i in range(0, N, B):
    for j in range(0, N, B):
        # Extraer el bloque
        bloque = matriz[i:i+B, j:j+B]
        
        # Solo procesar si el bloque tiene elementos no nulos
        if bloque.nnz > 0:
            procesar_bloque(bloque, i // B, j // B)
