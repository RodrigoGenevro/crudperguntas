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
        atualizar_treeview()
        messagebox.showinfo("Sucesso.","Pergunta adicionada com sucesso.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro ao adicionar a pergunta {e}")

def atualizar_pergunta():
    try:
        item = treeview.selection()
        if not item:
            messagebox.showerror("Erro", "Nenhuma pergunta selecionada.")
            return
        
        indice = treeview.index(item[0])

        nova = {
            "pergunta": pergunta.get(),
            "opcao1": opcao1.get(),
            "opcao2": opcao2.get(),
            "opcao3": opcao3.get(),
            "correta": int(correta.get())
        }

        logica.atualizar(perguntas, indice, nova)
        atualizar_treeview()
        messagebox.showinfo("Sucesso", "Pergunta atualizada.")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

def remover_pergunta():
    try:
        item = treeview.selection()
        if not item:
            messagebox.showerror("Erro", "Nenhuma pergunta selecionada.")
            return
        
        indice = treeview.index(item[0])
        logica.excluir(perguntas, indice)
        treeview.delete(item[0])
        atualizar_treeview()

        messagebox.showinfo("Sucesso", "Pergunta removida.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def atualizar_treeview():
    for item in treeview.get_children():
        treeview.delete(item)

    for p in perguntas:
        treeview.insert("", "end", values=(
            p["pergunta"],
            p["opcao1"],
            p["opcao2"],
            p["opcao3"],
            p["correta"]
        ))

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
    janela.geometry("1050x270")
    janela.configure(bg="#022a5c")

    style = ttk.Style()
    style.theme_use("default")
    
    pergunta = StringVar()
    opcao1 = StringVar()
    opcao2= StringVar()
    opcao3= StringVar()
    correta= IntVar()
    
    frame = Frame(janela,bg="#022a5c")
    frame.pack(fill="x", padx=10, pady=10)

    frame_botoes = Frame(janela,bg="#022a5c")
    frame_botoes.pack(fill="x")

    Label(janela, text="Cadastro / Edição de perguntas",bg="#022a5c",fg="white").pack()

    Label(frame, text="Pergunta:",bg="#022a5c",fg="white").grid(row=0, column=0)
    Entry(frame, textvariable=pergunta, width=50).grid(row=0, column=1, padx=10)

    Label(frame, text="Opção 1: ",bg="#022a5c",fg="white").grid(row=1, column=0)
    Entry(frame, textvariable=opcao1, width=50).grid(row=1,column=1, padx=10)

    Label(frame, text="Opção 2: ",bg="#022a5c",fg="white").grid(row=1, column=2)
    Entry(frame, textvariable=opcao2,width=50).grid(row=1, column=3, padx=10)
    
    Label(frame, text="Opção 3: ",bg="#022a5c",fg="white").grid(row=2, column=0)
    Entry(frame, textvariable=opcao3, width=50).grid(row=2,column=1, padx=10)

    Label(frame, text="Alternativa Correta: ",bg="#022a5c",fg="white").grid(row=2, column=2)
    Entry(frame, textvariable=correta,width=50).grid(row=2,column=3,padx=10)

    Button(frame_botoes, text="Adicionar Pergunta", command= adicionar_pergunta, bg="#29A50A", fg="white").grid(row=0,column=0, padx=15)
    Button(frame_botoes, text="Atualizar Pergunta", command= atualizar_pergunta, bg="#adad28", fg="white").grid(row=0,column=1)
    Button(frame_botoes, text="Remover Pergunta", command= remover_pergunta, bg="#b02121", fg="white").grid(row=0,column=2, padx=15)

    treeview = ttk.Treeview(janela, columns=("pergunta", "opcao1", "opcao2", "opcao3", "correta"), show="headings", height=6)
    treeview.heading("pergunta",text="Pergunta")
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