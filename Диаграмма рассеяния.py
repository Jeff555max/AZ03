# Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью
# функции `numpy.random.rand`
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100  # Количество точек для диаграммы рассеяния
x_data = np.random.rand(num_points)  # Случайные значения для оси X
y_data = np.random.rand(num_points)  # Случайные значения для оси Y

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='purple', alpha=0.7, edgecolor='black')
plt.title("Диаграмма рассеяния для случайных данных", fontsize=14)
plt.xlabel("X данные", fontsize=12)
plt.ylabel("Y данные", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
