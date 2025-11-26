import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import logica

def iniciar_interface():
    janela = tk.Tk()
    janela.title("CRUD de Perguntas")
    janela.geometry("850x500")

    perguntas = logica.carregar_dados()

    # == Interface ==
    frame = ttk.LabelFrame(janela, text= "Gerenciar Perguntas")
    frame.pack(fill="x", padx=10, pady=10)

    ttk.Label(frame, text="Pergunta:").grid(row=0, column=0)
    entrada_pergunta = ttk.Entry(frame, width=80)
    entrada_pergunta.grid(row=0, column=1, columnspan=3)

    # == Campos de texto ==
    Label(frame, text="Cadastro / Edição de Perguntas").grid(row=0, column=0, sticky="w")














    janela.mainloop()