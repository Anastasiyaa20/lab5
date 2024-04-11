import numpy as np
import matplotlib.pyplot as plt

def func_py(x: list[float], N: int) -> list[float]:
    """
    """
    return [np.sin(np.pi * xi / N) for xi in x]

def tabulate_py(a: float, b: float, n: int, N: int) -> tuple:
    x = [a + i*(b - a)/n for i in range(n)]
    y = func_py(x, N)
    return x, y

def main():
    a, b, n, N = 0, 1, 1000, 17

    fig, (ax1, ax2) = plt.subplots(2, 1)
    test_tabulation(tabulate_py, a, b, n, N, ax1)
    test_tabulation(tabulate_py, a, b, n, N, ax2)
    plt.show()

def test_tabulation(f, a, b, n, N, axis):
    res = f(a, b, n, N)
    axis.plot(res[0], res[1])
    axis.grid()

if __name__ == '__main__':
    main()
