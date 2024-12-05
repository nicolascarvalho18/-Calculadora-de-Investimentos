import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calcular_rendimento():
    try:
       
        valor_inicial = float(entry_valor_inicial.get())
        aporte_mensal = float(entry_aporte_mensal.get())
        taxa_juros = float(entry_taxa_juros.get()) / 100
        periodo = int(entry_periodo.get())

        saldo = [valor_inicial]
        meses = list(range(periodo + 1))

        for i in range(1, periodo + 1):
            saldo_anterior = saldo[-1]
            saldo_atual = saldo_anterior * (1 + taxa_juros) + aporte_mensal
            saldo.append(saldo_atual)

  
        saldo_final = saldo[-1]
        messagebox.showinfo("Resultado", f"Saldo final após {periodo} meses: R$ {saldo_final:.2f}")

    
        plt.figure(figsize=(8, 6))
        plt.plot(meses, saldo, marker="o", label="Rendimento")
        plt.title("Evolução do Investimento")
        plt.xlabel("Meses")
        plt.ylabel("Saldo (R$)")
        plt.grid(True)
        plt.legend()
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")


def limpar_campos():
    entry_valor_inicial.delete(0, tk.END)
    entry_aporte_mensal.delete(0, tk.END)
    entry_taxa_juros.delete(0, tk.END)
    entry_periodo.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora de Investimentos")
root.geometry("400x400")


tk.Label(root, text="Calculadora de Investimentos", font=("Arial", 16)).pack(pady=10)


tk.Label(root, text="Valor Inicial (R$):").pack()
entry_valor_inicial = tk.Entry(root)
entry_valor_inicial.pack()


tk.Label(root, text="Aporte Mensal (R$):").pack()
entry_aporte_mensal = tk.Entry(root)
entry_aporte_mensal.pack()


tk.Label(root, text="Taxa de Juros Mensal (%):").pack()
entry_taxa_juros = tk.Entry(root)
entry_taxa_juros.pack()

tk.Label(root, text="Período (meses):").pack()
entry_periodo = tk.Entry(root)
entry_periodo.pack()

tk.Button(root, text="Calcular", command=calcular_rendimento, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Limpar", command=limpar_campos, bg="red", fg="white").pack(pady=5)


tk.Label(root, text="© 2024 Calculadora de Investimentos", font=("Arial", 10)).pack(side="bottom", pady=10)


root.mainloop()
