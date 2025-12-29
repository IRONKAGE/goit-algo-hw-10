import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return x ** 2 # Функція для інтегрування

a = 0 # Нижня межа інтегрування
b = 2 # Верхня межа інтегрування

# --- Метод Монте-Карло ---
N = 100000  # Кількість випадкових точок

y_max = f(b)
area_rectangle = (b - a) * y_max

random_x = np.random.uniform(a, b, N)
random_y = np.random.uniform(0, y_max, N)

points_under_curve = np.sum(random_y <= f(random_x))

integral_mc = (points_under_curve / N) * area_rectangle
integral_analytical = 8/3
result_quad, error_quad = spi.quad(f, a, b)
x_vals = np.linspace(-0.5, 2.5, 400)
y_vals = f(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Приклад використання:
print("\n--- Оцінка інтеграла ---")
print(f"Оцінка інтеграла методом Монте-Карло (N={N}): {integral_mc}")
print(f"Аналітичний розрахунок інтеграла: {integral_analytical}")
print(f"Результат функції quad: {result_quad}")
print("\n--- Порівняльний аналіз ---")
print(f"Відмінність МК від аналітичного: {abs(integral_mc - integral_analytical)}")
print(f"Відмінність МК від quad: {abs(integral_mc - result_quad)}")
print("\n--- Щоб вийти, натисніть Ctrl+Z або Control+Z ---")

ax.set_xlim([x_vals[0], x_vals[-1]])
ax.set_ylim([0, max(y_vals) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid(True)
plt.show()
