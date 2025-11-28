import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

import logica

perguntas = logica.carregar_dados()

def adicionar_pergunta():
    try:
        nova_pergunta={
            "pergunta": pergunta.get(),
            "opcao1": opcao1.get(),
            "opcao2": opcao2.get(),
            "opcao3": opcao3.get(),
            "correta": int(correta.get())
        }
        logica.adicionar(perguntas, nova_pergunta)
        messagebox.showinfo("Sucesso.","Pergunta adicionada com sucesso.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro ao adicionar a pergunta {e}")

def mostrar_dados(event=None):
    selecao = treeview.selection()
    if not selecao:
        return
    
    item_id = selecao[0]
    valores = treeview.item(item_id, "values")

    pergunta.set(valores[0])
    opcao1.set(valores[1])
    opcao2.set(valores[2])
    opcao3.set(valores[3])
    correta.set(valores[4])

def iniciar_interface():
    global pergunta,opcao1,opcao2,opcao3,correta,treeview

    janela = tk.Tk()
    janela.title("CRUD de Perguntas")
    janela.geometry("850x500")
    
    pergunta = StringVar()
    opcao1 = StringVar()
    opcao2= StringVar()
    opcao3= StringVar()
    correta= IntVar()
    
    frame = Frame(janela)
    frame.pack(fill="x", padx=10, pady=10)

    Label(janela, text="Cadastro / Edição de perguntas").pack()

    Label(frame, text="Pergunta:").grid(row=0, column=0)
    Entry(frame, textvariable=pergunta, width=30).grid(row=0, column=1, padx=10,)

    Label(frame, text="Opção 1: ").grid(row=1, column=0)
    Entry(frame, textvariable=opcao1, width=30).grid(row=1,column=1, padx=10)

    Label(frame, text="Opção 2: ").grid(row=1, column=2)
    Entry(frame, textvariable=opcao2,width=30).grid(row=1, column=3, padx=10)
    
    Label(frame, text="Opção 3: ").grid(row=2, column=0)
    Entry(frame, textvariable=opcao3, width=30).grid(row=2,column=1, padx=10)

    Label(frame, text="Alternativa Correta: ").grid(row=2, column=2)
    Entry(frame, textvariable=correta,width=30).grid(row=2,column=3,padx=10)

    treeview = ttk.Treeview(janela, columns=("pergunta", "opcao1", "opcao2", "opcao3", "correta"), show="headings")
    treeview.heading("pergunta",text="pergunta")
    treeview.heading("opcao1", text="Opção 1")
    treeview.heading("opcao2", text="Opção 2")
    treeview.heading("opcao3", text="Opção 3")
    treeview.heading("correta",text="Resposta")
    treeview.pack(fill="both",padx=10,pady=10)

    treeview.bind("<<TreeviewSelect>>", mostrar_dados)
    for p in perguntas:
        treeview.insert("", "end", values=(p["pergunta"], p["opcao1"], p["opcao2"], p["opcao3"], p["correta"]))

    janela.mainloop()
iniciar_interface()