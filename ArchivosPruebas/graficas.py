import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_1 = 'PruebasQNodesN10.xlsx'
file_2 = 'PruebasQNodesCambiosFinales_10.xlsx'

data_1 = pd.read_excel(file_1)
data_2 = pd.read_excel(file_2)

perdida_1 = data_1['Perdida']
perdida_2 = data_2['Perdida']

particiones_1 = data_1['Particion']
particiones_2 = data_2['Particion']

tiempo_1 = data_1['Tiempo Total']
tiempo_2 = data_2['Tiempo Total']

# Gráfico para comparar la "Pérdida"
plt.figure(figsize=(10, 6))
plt.plot(perdida_1, label='Pérdida (Taller 1)', linestyle='-', marker='o', color='b', markersize=8)
plt.plot(perdida_2, label='Pérdida (Taller 2)', linestyle='-', marker='s', color='r', markersize=6)
plt.title("Comparación de Pérdida entre Taller 1 y Taller 2")
plt.ylabel("Valor de Pérdida")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico para comparar la "Particiones"
igualdad = np.array(particiones_1) == np.array(particiones_2)

plt.figure(figsize=(10, 3))
plt.plot(igualdad.astype(int), marker='o', linestyle='', color='green')
plt.title("Comparación de Igualdad entre Particiones (Taller 1 y Taller 2)")
plt.xlabel("Índice")
plt.ylabel("¿Iguales?")
plt.yticks([0, 1], ["No", "Sí"])
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de barras para comparar el "Tiempo Total"
plt.figure(figsize=(10, 6))
barWidth = 0.35

r1 = np.arange(len(tiempo_1))
r2 = [x + barWidth for x in r1]

plt.bar(r1, tiempo_1, color='b', width=barWidth, label='Tiempo Total (Taller 1)')
plt.bar(r2, tiempo_2, color='r', width=barWidth, label='Tiempo Total (Taller 2)')

plt.title("Cambio en el Tiempo Total entre Taller 1 y Taller 2")
plt.ylabel("Tiempo Total (segundos)")
plt.xticks([r + barWidth / 2 for r in range(len(tiempo_1))], [str(i) for i in range(1, len(tiempo_1) + 1)]) 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
