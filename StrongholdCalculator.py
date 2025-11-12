import math
import tkinter as tk
from tkinter import messagebox

def primera_opcion(c, hprimera, hsegunda):
    hprimera_rad = math.radians(hprimera)
    hsegunda_rad = math.radians(hsegunda)
    
    x = -(c / (math.tan(math.radians(90) - hprimera_rad) - math.tan(math.radians(90) - hsegunda_rad)))
    z = (c * (math.tan(math.radians(90) - hprimera_rad))) / (math.tan(math.radians(90) - hprimera_rad) - math.tan(math.radians(90) - hsegunda_rad))
    
    return x, z

def segunda_opcion(c, hprimera, hsegunda):
    hprimera_rad = math.radians(hprimera)
    hsegunda_rad = math.radians(hsegunda)
    
    x = (c * math.tan(hprimera_rad)) / (math.tan(hprimera_rad) - math.tan(hsegunda_rad))
    z = -(c / (math.tan(hprimera_rad) - math.tan(hsegunda_rad)))
    
    return x, z

def calcular(forma):
    try:
        
        c = float(entry_c.get())
        hprimera = float(entry_hprimera.get())
        hsegunda = float(entry_hsegunda.get())
        
        
        if forma == 1:
            x, z = primera_opcion(c, hprimera, hsegunda)
        elif forma == 2:
            x, z = segunda_opcion(c, hprimera, hsegunda)
        else:
            raise ValueError("Opción inválida")
        
        
        label_resultado.config(text=f"Resultado: x = {x:.2f}, z = {z:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

ventana = tk.Tk()
ventana.title("Calculadora Stronghold")

label_c = tk.Label(ventana, text="Distancia recorrida (c):")
label_c.grid(row=0, column=0, padx=10, pady=10)
entry_c = tk.Entry(ventana)
entry_c.grid(row=0, column=1, padx=10, pady=10)

label_hprimera = tk.Label(ventana, text="Ángulo primera enderpearl (hprimera en grados):")
label_hprimera.grid(row=1, column=0, padx=10, pady=10)
entry_hprimera = tk.Entry(ventana)
entry_hprimera.grid(row=1, column=1, padx=10, pady=10)

label_hsegunda = tk.Label(ventana, text="Ángulo segunda enderpearl (hsegunda en grados):")
label_hsegunda.grid(row=2, column=0, padx=10, pady=10)
entry_hsegunda = tk.Entry(ventana)
entry_hsegunda.grid(row=2, column=1, padx=10, pady=10)

boton_opcion1 = tk.Button(ventana, text="Calcular con opción 1", command=lambda: calcular(1))
boton_opcion1.grid(row=3, column=0, padx=10, pady=10)

boton_opcion2 = tk.Button(ventana, text="Calcular con opción 2", command=lambda: calcular(2))
boton_opcion2.grid(row=3, column=1, padx=10, pady=10)

label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14))
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

ventana.mainloop()
