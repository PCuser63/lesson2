import numpy as np
import matplotlib.pyplot as plt

# Определение функции
def f(x, y):
    return 1/4 * np.sin(0.5 * x**2 - y) - np.exp(-((x-5)**2 + (y-2)**2))

# Создание сетки координат
x = np.linspace(2, 8, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Построение графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()
