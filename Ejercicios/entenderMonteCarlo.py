import numpy as np

N = 100000000
x = np.random.rand(N)
y = np.random.rand(N)
dentro_circulo = (x**2 + y**2) <= 1
pi_aproximado = 4 * np.sum(dentro_circulo) / N
print("π ≈", pi_aproximado)
