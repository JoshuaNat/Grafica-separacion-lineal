import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import tkinter as tk
import numpy as np

#Variable global para almacenar las coordenadas
Xs = []

def on_click(event):
    if event.inaxes is not None:
        #Agrega las coordenadas a la lista
        Xs.append([1, event.xdata, event.ydata])
        plt.plot(event.xdata, event.ydata, 'ok')
        canvas.draw()
    else:
        print ('Clicked ouside axes bounds but inside plot window')

def graficar_linea():
    crear_grafica()

    w1 = float(peso_1.get("1.0", "end-1c"))
    w2 = float(peso_2.get("1.0", "end-1c"))
    b = float(bias.get("1.0", "end-1c"))

    m = -w1/w2
    c = -b/w2

    plt.axline((0,c), slope=m, linewidth = 4)
    canvas.draw()
    prod_p(w1, w2, b)


def prod_p(p1, p2, b):
    if Xs:
        W = np.array([b, p1, p2])
        X = np.array(Xs)
        y = np.dot(W, X.T) >= 0
        
        for i in range(len(y)):
            if (y[i] == 0):
                plt.plot(X[i][1], X[i][2], 'or')
            else:
                plt.plot(X[i][1], X[i][2], 'ob')
    
    canvas.draw()

def crear_grafica():
    plt.clf()
    plt.title("Practica 1")
    plt.grid("on")
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.xlabel(r"x1")
    plt.ylabel(r"x2")
    plt.draw()

def limpiar():
    ms1 = "W1"
    ms2 = "W2"
    ms3 = "Bias"
    Xs.clear()
    peso_1.delete("1.0", "end-1c")
    peso_1.insert(tk.END, ms1)
    peso_2.delete("1.0", "end-1c")
    peso_2.insert(tk.END, ms2)
    bias.delete("1.0", "end-1c")
    bias.insert(tk.END, ms3)
    crear_grafica()

# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()
fig, ax = plt.subplots()
 
# Tkinter Application
frame = tk.Frame(root)
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
graficar = tk.Button(root, height=2, width=15, text="Graficar", command=lambda:graficar_linea())
graficar.pack()
resetear = tk.Button(root, height=2, width=15, text="Reiniciar", command=lambda:limpiar())
resetear.pack()
 
# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 
# Plot data on Matplotlib Figure
t = np.arange(0, 2*np.pi, .01)
crear_grafica()
fig.canvas.callbacks.connect('button_press_event', on_click)
canvas.draw()
 
root.mainloop()