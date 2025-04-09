import numpy as np
from scipy.sparse import random, csr_matrix
from scipy.optimize import minimize, Bounds
from multiprocessing import Pool, cpu_count, current_process
import os
import time

# Configuración general
n = 5
N = n * (2 ** n)
B = 16  # Tamaño de bloque
density = 0.01
A = random(N, N, density=density, format='csr')
b = np.random.rand(N)

# Preparar bloques con datos
bloques = [(A[i:i+B, i:i+B], b[i:i+B], i) for i in range(0, N, B) if A[i:i+B, i:i+B].nnz > 0]

# Función paralela
def procesar_bloque(args):
    bloque, b_sub, idx = args
    proc_id = os.getpid()
    print(f"[Proceso {proc_id}] ➤ INICIO bloque {idx} ⏱️ {time.strftime('%H:%M:%S')}")

    if bloque.nnz == 0:
        print(f"[Proceso {proc_id}] ❌ Bloque {idx} vacío.")
        return (idx, None)

    # Normalización
    # Esto evita que los valores de la matriz y el vector sean muy grandes y causen errores como overflow.
    max_val = bloque.max()
    if max_val != 0:
        bloque = bloque / max_val
        b_sub = b_sub / b_sub.max()

    x0 = np.random.uniform(-1, 1, size=bloque.shape[0])
    limites = Bounds(-10*np.ones_like(x0), 10*np.ones_like(x0))

    def f(x):
        return 0.5 * x @ (bloque @ x) - b_sub @ x

    try:
        res = minimize(f, x0, method="L-BFGS-B", bounds=limites)
        valor = res.fun if res.success else np.nan
    except Exception as e:
        print(f"[Proceso {proc_id}] ⚠️ Error en bloque {idx}: {e}")
        valor = np.nan

    print(f"[Proceso {proc_id}] ✅ FIN bloque {idx} ✔️ valor óptimo = {valor:.4f} 🕓 {time.strftime('%H:%M:%S')}")
    return (idx, valor)

# Paralelizar
if __name__ == "__main__":
    print(f"\n🌐 Procesos disponibles: {cpu_count()}")
    print(f"🔢 Bloques a procesar: {len(bloques)}\n")

    start_time = time.time()
    with Pool(processes=cpu_count()) as pool:
        resultados = pool.map(procesar_bloque, bloques)

    print(f"\n✅ Total de bloques procesados: {len(resultados)}")
    print(f"⏳ Tiempo total: {time.time() - start_time:.2f} segundos")

    # Mostrar resumen de los resultados
    for idx, valor in resultados:
        print(f"🧩 Bloque {idx}: valor óptimo = {valor}")
        

