# DM_project
Алгоритм Уоршелла. Мацко, Конахович, Ушкевич
import random
import copy


class Graph:
    def __init__(self, num_vertices):
        """
        Конструктор: створює пусту матрицю (таблицю) розміром n на n.
        Спочатку всюди нулі (зв'язків немає).
        """
        self.n = num_vertices  # Кількість вершин (n)
        # Створюємо матрицю суміжності: список списків, заповнений 0
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def generate_random(self, density):
        """
        Генерує випадковий граф (Етап 2 завдання).
        density - це щільність від 0.0 до 1.0 (наприклад, 0.2 = 20% зв'язків).
        """
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    self.matrix[i][j] = 0  # Петлі (шлях сам у себе) зазвичай 0 у простих графах
                else:
                    # random.random() видає число від 0 до 1.
                    # Якщо воно менше за density, ставимо 1 (зв'язок є).
                    if random.random() < density:
                        self.matrix[i][j] = 1
                    else:
                        self.matrix[i][j] = 0

    def print_matrix(self, matrix_to_print, title="Матриця"):
        """
        Допоміжна функція просто для красивого виводу таблички в консоль.
        """
        print(f"\n--- {title} ---")
        # Друкуємо шапку (номери стовпчиків)
        print("   ", end="")
        for i in range(len(matrix_to_print)):
            print(f"{i:2}", end=" ")
        print()

        # Друкуємо рядки
        for i in range(len(matrix_to_print)):
            print(f"{i:2}|", end=" ")  # Номер рядка
            for val in matrix_to_print[i]:
                # Виводимо 1 або 0. "." для нуля, щоб краще видно було структуру
                print(f"{1 if val else '.' :2}", end=" ")
            print()

    def warshall_algorithm(self):
        """
        Етап 3: Реалізація алгоритму Уоршелла.
        Будує матрицю досяжності (транзитивне замикання).
        """
        # Робимо копію матриці, щоб не зіпсувати початкову
        R = copy.deepcopy(self.matrix)

        n = self.n

        # Три вкладені цикли - це і є весь алгоритм!
        for k in range(n):  # k - це проміжна вершина, через яку пробуємо пройти
            for i in range(n):  # i - звідки виходимо
                for j in range(n):  # j - куди йдемо

                    # Логіка: Шлях i->j існує, якщо:
                    # Він вже був (R[i][j])
                    # АБО (or)
                    # Є шлях з i в k (R[i][k]) І (and) шлях з k в j (R[k][j])

                    R[i][j] = R[i][j] or (R[i][k] and R[k][j])

        return R


# --- Блок перевірки (те, що запуститься) ---

if __name__ == "__main__":
    # 1. Створюємо граф на 5 вершин (маленький, щоб було видно очима)
    my_graph = Graph(num_vertices=5)

    # 2. Генеруємо випадкові зв'язки з щільністю 0.3 (30% заповненості)
    # [cite: 73] - вимога завдання про параметр щільності
    my_graph.generate_random(density=0.3)

    # 3. Виводимо початковий вигляд (хто з ким з'єднаний напряму)
    my_graph.print_matrix(my_graph.matrix, "Початкова Матриця Суміжності")

    # 4. Запускаємо алгоритм Уоршелла
    reachability_matrix = my_graph.warshall_algorithm()

    # 5. Виводимо результат (куди взагалі можна дійти, якщо робити пересадки)
    my_graph.print_matrix(reachability_matrix, "Матриця Досяжності (Уоршелл)")

    print("\nГотово! Якщо ви бачите більше одиничок у другій таблиці, алгоритм працює.")

------------------------------------------------------

    import random
import time
import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, n, directed=True):
        self.n = n
        self.directed = directed
        self.adj_matrix = [[0]*n for _ in range(n)]
        self.adj_list = [[] for _ in range(n)]

    # ---------------------------
    # Додавання ребра
    # ---------------------------
    def add_edge(self, u, v):
        if self.adj_matrix[u][v] == 0:
            self.adj_matrix[u][v] = 1
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_matrix[v][u] = 1
                self.adj_list[v].append(u)

    # ---------------------------
    # Генерація випадкового орієнтованого графа
    # ---------------------------
    def generate_random(self, delta):
        max_edges = self.n * (self.n - 1)
        m = int(max_edges * delta)
        possible_edges = [(i,j) for i in range(self.n) for j in range(self.n) if i != j]
        chosen_edges = random.sample(possible_edges, m)
        for u,v in chosen_edges:
            self.add_edge(u,v)

    # ---------------------------
    # Алгоритм Уоршелла
    # ---------------------------
    def warshall(self):
        reach = [row[:] for row in self.adj_matrix]  # копія матриці
        n = self.n
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if reach[i][k] and reach[k][j]:
                        reach[i][j] = 1
        return reach

    # ---------------------------
    # Друк матриці у терміналі
    # ---------------------------
    def print_matrix(self):
        print("Adjacency Matrix:")
        header = "   " + " ".join(f"{i:2}" for i in range(self.n))
        print(header)
        for i, row in enumerate(self.adj_matrix):
            print(f"{i:2} " + " ".join(str(val) for val in row))

    # ---------------------------
    # Візуалізація матриці кольоровою картою
    # ---------------------------
    def plot_matrix(self, matrix=None, title="Adjacency Matrix"):
        if matrix is None:
            matrix = self.adj_matrix
        plt.figure(figsize=(6,6))
        plt.imshow(matrix, cmap='Blues', interpolation='none')
        plt.title(title)
        plt.xlabel("To Vertex")
        plt.ylabel("From Vertex")
        plt.colorbar(label='Edge')
        plt.show()


# ---------------------------
# Експеримент: вимір часу алгоритму Уоршелла
# ---------------------------
def run_experiment(sizes, delta):
    print(f"{'n':>5} | {'Edges':>6} | {'Time (s)':>10}")
    print("-"*30)
    for n in sizes:
        g = Graph(n, directed=True)
        g.generate_random(delta)
        num_edges = sum(len(neigh) for neigh in g.adj_list)
        start_time = time.perf_counter()
        reach_matrix = g.warshall()
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"{n:5} | {num_edges:6} | {elapsed:10.6f}")

        # Візуалізація маленьких графів
        if n <= 20:  # щоб не було занадто великих карт
            g.print_matrix()
            g.plot_matrix(title=f"Graph n={n}")


# ---------------------------
# Приклад запуску
# ---------------------------
if __name__ == "__main__":
    sizes = [10, 15, 50]  # для маленьких n показуємо матрицю
    delta = 0.2            # щільність 20%
    run_experiment(sizes, delta)

