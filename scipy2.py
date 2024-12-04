import numpy as np
import matplotlib.pyplot as plt

def read_system_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    N = int(lines[0].strip())
    A = np.array([list(map(float, line.strip().split())) for line in lines[1:N+1]])
    b = np.array(list(map(float, lines[N+1].strip().split())))
    return A, b

def solve_linear_system(A, b):
    x = np.linalg.solve(A, b)
    return x

def plot_solution(x):
    plt.bar(range(len(x)), x)
    plt.grid()
    plt.xlabel('Номер элемента')
    plt.ylabel('Значение')
    plt.title('Решение СЛАУ')
    plt.show()

A, b = read_system_from_file('C:\\Users\Professional\Downloads\large.txt')
x = solve_linear_system(A, b)
plot_solution(x)