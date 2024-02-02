import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
import tkinter as tk
import numpy as np

def on_click(event):
    if event.inaxes is not None:
        print (event.xdata, event.ydata)
    else:
        print ('Clicked ouside axes bounds but inside plot window')
 
# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()
fig, ax = plt.subplots()
 
# Tkinter Application
frame = tk.Frame(root)
label = tk.Label(text = "Matplotlib + Tkinter!")
label.config(font=("Courier", 32))
label.pack()
frame.pack()
 
# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 
# Plot data on Matplotlib Figure
t = np.arange(0, 2*np.pi, .01)
ax.plot(t, np.sin(t))
fig.canvas.callbacks.connect('button_press_event', on_click)
canvas.draw()
 
root.mainloop()