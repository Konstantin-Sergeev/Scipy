import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)
ode = sp.Eq(y.diff(x), -2 * y)
solution_sym = sp.dsolve(ode, y, ics={y.subs(x, 0): sp.sqrt(2)})
y_sym = sp.lambdify(x, solution_sym.rhs, 'numpy')

def dydx(t, y): return -2 * y
sol = solve_ivp(dydx, [0, 10], [np.sqrt(2)], t_eval=np.linspace(0, 10, 100))

t = np.linspace(0, 10, 100)
y_scipy = sol.y[0]
y_symbolic = y_sym(t)

plt.figure(figsize=(11, 8))
plt.plot(t, y_symbolic, label='SymPy', linestyle='--')
plt.plot(sol.t, y_scipy, label='SciPy', linestyle=':')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Решения дифура')
plt.legend()
plt.grid()

plt.figure(figsize=(11, 8))
plt.plot(sol.t, y_symbolic - y_scipy, label='Разность (SymPy - SciPy)')
plt.xlabel('x')
plt.ylabel('Разность')
plt.title('Разность между решениями SciPy и SymPy')
plt.legend()
plt.grid()
plt.show()