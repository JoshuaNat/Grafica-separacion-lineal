import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import tkinter as tk
import numpy as np

def on_click(event):
    if event.inaxes is not None:
        print (event.xdata, event.ydata)
        plt.plot(event.xdata, event.ydata, 'or')
        canvas.draw()
    else:
        print ('Clicked ouside axes bounds but inside plot window')

def graficar_linea():
    pass
 
# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()
fig, ax = plt.subplots()
 
# Tkinter Application
frame = tk.Frame(root)
#label = tk.Label(text = "Matplotlib + Tkinter!")
#label.config(font=("Courier", 32))
#label.pack()
frame.pack()

#Creaciones de texto
peso_1 = tk.Text(root, height = 1, width = 15)
peso_2 = tk.Text(root, height = 1, width = 15)
bias = tk.Text(root, height = 1, width = 15)
ms1 = "W1"
ms2 = "W2"
ms3 = "Bias"
peso_1.pack()
peso_1.insert(tk.END, ms1)
peso_2.pack()
peso_2.insert(tk.END, ms2)
bias.pack()
bias.insert(tk.END, ms3)

#Creación del boton
graficar = tk.Button(root, height=2, width=15, text="Graficar")
graficar.pack()
 
# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 
# Plot data on Matplotlib Figure
t = np.arange(0, 2*np.pi, .01)
plt.xlim([-2,2])
plt.ylim([-2,2])
fig.canvas.callbacks.connect('button_press_event', on_click)
canvas.draw()
 
root.mainloop()