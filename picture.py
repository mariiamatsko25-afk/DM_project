import matplotlib.pyplot as plt
import numpy as np

# --- ВХІДНІ ДАНІ (Твої результати) ---
vertices = [50, 60, 70, 80, 100, 120, 140, 150, 170, 190]
densities = [30, 40, 50, 60, 70]

# Дані часу (по стовпцях з твоєї таблиці)
times_30 = [0.007653, 0.014067, 0.019590, 0.026660, 0.055570, 0.090316, 0.147788, 0.181093, 0.248542, 0.366495]
times_40 = [0.007571, 0.014507, 0.019026, 0.028237, 0.051864, 0.088905, 0.140655, 0.185767, 0.245255, 0.351014]
times_50 = [0.008159, 0.011294, 0.018471, 0.025374, 0.054878, 0.092349, 0.132074, 0.191874, 0.253443, 0.361669]
times_60 = [0.007055, 0.012174, 0.017461, 0.027464, 0.053681, 0.109896, 0.155033, 0.174073, 0.246096, 0.374134]
times_70 = [0.008367, 0.012106, 0.019652, 0.028870, 0.051026, 0.102608, 0.144467, 0.170492, 0.261822, 0.366938]

# Збираємо дані для останнього зрізу (N=190) для графіка щільності
i = 9
times_at_190 = [times_30[i], times_40[i], times_50[i], times_60[i], times_70[i]]

# ==========================================
# ГРАФІК 1: Залежність часу від кількості вершин
# ==========================================
plt.figure(figsize=(10, 6))
plt.plot(vertices, times_30, marker='o', label='30% щільності')
plt.plot(vertices, times_40, marker='s', label='40% щільності')
plt.plot(vertices, times_50, marker='^', label='50% щільності')
plt.plot(vertices, times_60, marker='x', label='60% щільності')
plt.plot(vertices, times_70, marker='d', label='70% щільності')

# Додаємо теоретичну криву O(n^3) пунктиром
k = 0.36 / (190**3) # Коефіцієнт масштабування
x_theory = np.linspace(50, 190, 100)
y_theory = k * (x_theory ** 3)
plt.plot(x_theory, y_theory, 'k--', linewidth=2, alpha=0.7, label='Теоретична O(n³)')

plt.title('Рис 1. Залежність часу виконання від розміру графа', fontsize=14)
plt.xlabel('Кількість вершин (n)', fontsize=12)
plt.ylabel('Час (сек)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('graph_time_vs_n.png', dpi=300) # Зберігає файл
print("Збережено: graph_time_vs_n.png")
plt.close()

# ==========================================
# ГРАФІК 2: Залежність часу від щільності (для N=190)
# ==========================================
plt.figure(figsize=(8, 5))
plt.plot(densities, times_at_190, color='purple', marker='D', markersize=8, linewidth=2)

# Налаштування осей, щоб показати "стабільність"
plt.ylim(0, 0.5) # Фіксуємо вісь Y, щоб показати, що коливання незначні

plt.title('Рис 2. Вплив щільності на час (при N=190)', fontsize=14)
plt.xlabel('Щільність графа (%)', fontsize=12)
plt.ylabel('Час (сек)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Додаємо підпис значень
for i, txt in enumerate(times_at_190):
    plt.annotate(f"{txt:.3f}с", (densities[i], times_at_190[i]),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.savefig('graph_time_vs_density.png', dpi=300)
print("Збережено: graph_time_vs_density.png")
plt.close()

# ==========================================
# ГРАФІК 3: Теоретичне порівняння O(n^2) та O(n^3)
# ==========================================
plt.figure(figsize=(8, 5))
x = np.linspace(0, 200, 100)
y_cube = x**3
y_square = x**2 * 100 # Множимо на 100, щоб хоч трохи було видно на фоні куба

plt.plot(x, y_cube, 'r-', linewidth=2, label='O(n³) - Уоршелл')
plt.plot(x, y_square, 'b--', linewidth=2, label='O(n²) - Просто читання матриці')

plt.title('Рис 3. Теоретичне зростання складності', fontsize=14)
plt.xlabel('Розмір вхідних даних (n)', fontsize=12)
plt.ylabel('Кількість операцій (умовні одиниці)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.5)
plt.fill_between(x, y_cube, color='red', alpha=0.1) # Зафарбувати область під графіком

plt.tight_layout()
plt.savefig('graph_theory_comparison.png', dpi=300)
print("Збережено: graph_theory_comparison.png")
plt.close()

print("\nВсі графіки успішно створено!")
