import numpy as np 
import matplotlib.pyplot as plt 
import timeit 
 
def func_py(x: list[float], N: int) -> list[float]: 
    """ 
    Calculate function values for passed array of arguments 
    """ 
    return [np.sin(np.pi * xi / N) for xi in x] 
  
def tabulate_py(a: float, b: float, n: int, N: int) -> tuple[float]: 
    x = [a + x*(b - a)/n for x in range(n)] 
    y = func_py(x, N) 
    return x, y 
 
def tabulate_np(a: float, b: float, n: int) -> tuple[np.ndarray]: 
    x = np.linspace(a, b, n) 
    y = x / (x**2 + 1) 
    return x, y 
 
def main(): 
    a, b = 0, 1 
    n = np.array((1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000), dtype="uint32") 
    t_py = np.full_like(n, 0, dtype=float) 
    t_np = np.full_like(n, 0, dtype=float) 
    for i in range(len(n)): 
        t_py[i] = 1_000_000 * timeit.timeit(f"tabulate_py(0, 1, {n[i]}, 17)", number=100, globals=globals()) / 100 
        t_np[i] = 1_000_000 * timeit.timeit(f"tabulate_np(0, 1, {n[i]})", number=100, globals=globals()) / 100 
 
    plt.plot(n, t_py/t_np) 
    plt.grid() 
    plt.show() 
 
if __name__ == '__main__': 
    main()
