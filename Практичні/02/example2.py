import numpy as np
import matplotlib.pyplot as plt

def get_function_input():
    func_input = input("Введіть функцію у форматі '2*x + 1': ")
    return func_input

def get_x_range_input():
    x_range_input = input("Введіть діапазон для x у форматі '-5 5': ")
    x_min, x_max = map(float, x_range_input.split())
    return x_min, x_max

def build_plot(func_input, x_min, x_max):
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

def menu():
    func_input = None
    x_min = x_max = None

    while True:
        print("\nМеню:")
        print("1. Ввести формулу")
        print("2. Вибрати діапазон для x")
        print("3. Побудувати графік")
        print("4. Вийти")

        choice = input("Зробіть вибір: ")

        if choice == '1':
            func_input = get_function_input()
        elif choice == '2':
            x_min, x_max = get_x_range_input()
        elif choice == '3':
            if func_input and x_min is not None and x_max is not None:
                build_plot(func_input, x_min, x_max)
            else:
                print("Спочатку введіть формулу і діапазон для x.")
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    menu()
