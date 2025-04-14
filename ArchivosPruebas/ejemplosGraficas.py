import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)
data = np.random.randn(1000)

# Gráfico de líneas
plt.plot(x, y)
plt.title('Gráfico de líneas')
plt.show()

# Gráfico de dispersión
plt.scatter(x, y)
plt.title('Gráfico de dispersión')
plt.show()

# Gráfico de barras
plt.bar([1, 2, 3], [4, 5, 6])
plt.title('Gráfico de barras')
plt.show()

# Histograma
plt.hist(data, bins=30)
plt.title('Histograma')
plt.show()

# Gráfico de torta
labels = ['A', 'B', 'C']
sizes = [10, 20, 70]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Gráfico de torta')
plt.show()

# Boxplot
plt.boxplot(data)
plt.title('Boxplot')
plt.show()
