import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import simpledialog, messagebox

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Об'єктно-орієнтований інтерфейс для побудови графіків")
        
        self.figure, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        self.graphs = []  
        self.dragging = False  

        self.add_button = tk.Button(root, text="Додати графік", command=self.add_graph)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(root, text="Очистити графіки", command=self.clear_graphs)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_drag)

    def add_graph(self):
        formula = simpledialog.askstring("Введіть функцію", "Введіть формулу у форматі '2*x + 3':")
        if formula:
            self.graphs.append(formula)
            self.plot_graphs()

    def plot_graphs(self):
        self.ax.clear()  
        x = np.linspace(-10, 10, 400)
        for formula in self.graphs:
            try:
                y = eval(formula)
                self.ax.plot(x, y, label=f'y = {formula}')
            except Exception as e:
                messagebox.showerror("Помилка", f"Помилка у формулі: {e}")

        self.ax.set_title('Графіки функцій')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()

    def clear_graphs(self):
        self.graphs = []  
        self.ax.clear()   
        self.canvas.draw()

    def on_click(self, event):
        if event.inaxes:
            self.start_x, self.start_y = event.xdata, event.ydata
            self.dragging = True

    def on_drag(self, event):
        if self.dragging and event.inaxes:
            dx = event.xdata - self.start_x
            dy = event.ydata - self.start_y
            self.start_x, self.start_y = event.xdata, event.ydata

            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
            self.ax.set_ylim(ylim[0] - dy, ylim[1] - dy)
            self.canvas.draw()

        if event.button == 1 and not event.inaxes:
            self.dragging = False

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
