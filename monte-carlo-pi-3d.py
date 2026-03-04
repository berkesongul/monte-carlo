import matplotlib.pyplot as plt
import numpy as np

# Simülasyon parametreleri
n_points = 2000
x = np.random.uniform(-1, 1, n_points)
y = np.random.uniform(-1, 1, n_points)
z = np.random.uniform(-1, 1, n_points)

# Kürenin içinde mi kontrol et (x^2 + y^2 + z^2 <= r^2)
inside = x**2 + y**2 + z**2 <= 1
hits = np.sum(inside)
pi_estimate = 6 * (hits / n_points)

# 3D Görselleştirme
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# İçeridekiler kırmızı, dışarıdakiler mavi
ax.scatter(x[inside], y[inside], z[inside], c='r', marker='o', s=10, alpha=0.5, label='Küre İçinde')
ax.scatter(x[~inside], y[~inside], z[~inside], c='b', marker='^', s=10, alpha=0.2, label='Dışında')

ax.set_title(f"3D Monte Carlo Pi Tahmini: {pi_estimate:.4f}")
plt.legend()
plt.show()