import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Побудова графіка функції")

        self.formula_label = tk.Label(root, text="Введіть формулу:")
        self.formula_label.pack(pady=5)

        self.formula_entry = tk.Entry(root, width=30)
        self.formula_entry.pack(pady=5)

        self.range_frame = tk.Frame(root)
        self.range_frame.pack(pady=10)

        self.xmin_label = tk.Label(self.range_frame, text="X min:")
        self.xmin_label.grid(row=0, column=0, padx=5)

        self.xmin_slider = tk.Scale(self.range_frame, from_=-100, to=100, orient=tk.HORIZONTAL)
        self.xmin_slider.set(-10)
        self.xmin_slider.grid(row=0, column=1, padx=5)

        self.xmax_label = tk.Label(self.range_frame, text="X max:")
        self.xmax_label.grid(row=0, column=2, padx=5)

        self.xmax_slider = tk.Scale(self.range_frame, from_=-100, to=100, orient=tk.HORIZONTAL)
        self.xmax_slider.set(10)
        self.xmax_slider.grid(row=0, column=3, padx=5)

        self.plot_button = tk.Button(root, text="Побудувати графік", command=self.plot_graph)
        self.plot_button.pack(pady=10)

        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

        self.color_button = tk.Button(root, text="Змінити колір лінії", command=self.change_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.style_button = tk.Button(root, text="Змінити стиль лінії", command=self.change_style)
        self.style_button.pack(side=tk.RIGHT, padx=5, pady=10)

        self.line_color = 'blue'
        self.line_style = '-'

    def plot_graph(self):
        self.ax.clear()

        formula = self.formula_entry.get()
        x_min = self.xmin_slider.get()
        x_max = self.xmax_slider.get()

        x = np.linspace(x_min, x_max, 400)
        try:
            y = eval(formula)
            self.ax.plot(x, y, color=self.line_color, linestyle=self.line_style)
            self.ax.set_title(f'Графік функції: {formula}')
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('y')
            self.ax.grid(True)

            self.canvas.draw()
        except Exception as e:
            tk.messagebox.showerror("Помилка", f"Помилка у формулі: {e}")

    def change_color(self):
        colors = ['blue', 'red', 'green', 'purple', 'orange']
        current_color_index = colors.index(self.line_color)
        new_color_index = (current_color_index + 1) % len(colors)
        self.line_color = colors[new_color_index]
        self.plot_graph()

    def change_style(self):
        styles = ['-', '--', '-.', ':']
        current_style_index = styles.index(self.line_style)
        new_style_index = (current_style_index + 1) % len(styles)
        self.line_style = styles[new_style_index]
        self.plot_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
