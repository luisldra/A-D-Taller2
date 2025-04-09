import numpy as np
from scipy.sparse import random, csr_matrix
from scipy.optimize import minimize, Bounds
from multiprocessing import Pool, cpu_count
import os
import time
import matplotlib.pyplot as plt
import psutil
import random as rnd

# Función para procesar un bloque
def procesar_bloque(args):
    bloque, b_sub, idx = args
    if bloque.nnz == 0:
        return (idx, None)

    max_val = bloque.max()
    if max_val != 0:
        bloque = bloque / max_val
        b_sub = b_sub / b_sub.max()

    x0 = np.random.uniform(-1, 1, size=bloque.shape[0])
    limites = Bounds(-10*np.ones_like(x0), 10*np.ones_like(x0))

    def f(x):
        return 0.5 * x @ (bloque @ x) - b_sub @ x

    res = minimize(f, x0, method="L-BFGS-B", bounds=limites)
    return (idx, res.fun if res.success else np.nan)

# Función que ejecuta un enfoque (exhaustivo o muestreo)
def ejecutar_estrategia(nombre, bloques, usar_muestreo=False, fraccion=0.1):
    print(f"\n🔍 Ejecutando estrategia: {nombre}")
    if usar_muestreo:
        bloques = rnd.sample(bloques, int(len(bloques) * fraccion))
        print(f"🎲 Muestreo Monte Carlo: {len(bloques)} bloques seleccionados")

    t0 = time.time()
    mem0 = psutil.Process(os.getpid()).memory_info().rss / (1024**2)

    with Pool(processes=cpu_count()) as pool:
        resultados = pool.map(procesar_bloque, bloques)

    mem1 = psutil.Process(os.getpid()).memory_info().rss / (1024**2)
    tf = time.time()

    tiempo = tf - t0
    memoria = mem1 - mem0

    print(f"✅ {nombre} completado en {tiempo:.2f}s | Memoria usada: {memoria:.2f} MB")
    return resultados, tiempo, memoria

# ------------------------ MAIN ------------------------ #
if __name__ == "__main__":
    # Parámetros
    n = 5
    N = n * (2 ** n)
    B = 64
    density = 0.01

    # Crear matriz dispersa
    A = random(N, N, density=density, format='csr')
    b = np.random.rand(N)

    # Crear bloques no vacíos
    bloques = [
        (A[i:i+B, i:i+B], b[i:i+B], i)
        for i in range(0, N, B)
        if A[i:i+B, i:i+B].nnz > 0
    ]
    print(f"\n🧱 Total de bloques no vacíos: {len(bloques)}")

    # Ejecutar estrategia 1: EXHAUSTIVA
    resultados_ex, tiempo_ex, mem_ex = ejecutar_estrategia("Exhaustiva", bloques)

    # Ejecutar estrategia 2: MONTE CARLO (10%)
    resultados_mc, tiempo_mc, mem_mc = ejecutar_estrategia("Monte Carlo", bloques, usar_muestreo=True, fraccion=0.1)

    # Visualización de resultados
    etiquetas = ['Exhaustivo', 'Monte Carlo']
    tiempos = [tiempo_ex, tiempo_mc]
    memorias = [mem_ex, mem_mc]

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.bar(etiquetas, tiempos)
    plt.title("⏳ Tiempo (segundos)")
    plt.ylabel("Segundos")

    plt.subplot(1, 2, 2)
    plt.bar(etiquetas, memorias)
    plt.title("💾 Uso de memoria (MB)")
    plt.ylabel("Megabytes")

    plt.tight_layout()
    plt.show()

    # Mostrar primeros resultados
    print("\n📊 Muestra de resultados (primeros bloques):")
    for idx, val in resultados_mc[:5]:
        print(f"Bloque {idx}: Valor óptimo ≈ {val}")
