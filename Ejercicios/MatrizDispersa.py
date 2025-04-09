import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix

# Parámetro n
n = 4
size = n * (2 ** n)

# Crear una matriz dispersa aleatoria con valores en posiciones específicas
# Solo se llena un 1% de las entradas
density = 0.01
num_entries = int(size * size * density)

# Indices aleatorios para filas y columnas
rows = np.random.randint(0, size, num_entries)
cols = np.random.randint(0, size, num_entries)
data = np.random.rand(num_entries)

# Creamos la matriz dispersa
sparse_matrix = csr_matrix((data, (rows, cols)), shape=(size, size))

# Mostrar información
print(f"Matriz de tamaño: {size} x {size}")
print(f"Número de elementos no nulos: {sparse_matrix.count_nonzero()}")

# Visualización
plt.figure(figsize=(6, 6))
plt.spy(sparse_matrix, markersize=1)
plt.title("Visualización de matriz dispersa")
plt.show()
