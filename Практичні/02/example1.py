import numpy as np
import matplotlib.pyplot as plt

def main():
    func_input = input("Введіть функцію у форматі '2*x + 1': ")
    x_range_input = input("Введіть діапазон для x у форматі '-5 5': ")
    
    x_min, x_max = map(float, x_range_input.split())
    
    x = np.linspace(x_min, x_max, 400)
    
    try:
        y = eval(func_input)
    except Exception as e:
        print(f"Помилка у формулі: {e}")
        return
    
    plt.plot(x, y, label=f'y = {func_input}')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Графік функції')
    plt.legend()
    
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
