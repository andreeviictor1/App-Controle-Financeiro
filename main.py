import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from crud import (adicionar_receita, adicionar_despesa, visualizar_receitas, 
                  visualizar_despesas, gerar_relatorio, deletar_receita, deletar_despesa)

def adicionar_receita_interface():
    def adicionar():
        data = entry_data.get()
        valor = float(entry_valor.get())
        descricao = entry_descricao.get()
        adicionar_receita(data, valor, descricao)
        messagebox.showinfo("Sucesso", "Receita adicionada com sucesso!")
        janela_adicionar.destroy()

    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Receita")
    
    tk.Label(janela_adicionar, text="Data").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(janela_adicionar, text="Valor").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(janela_adicionar, text="Descrição").grid(row=2, column=0, padx=10, pady=5)
    
    entry_data = tk.Entry(janela_adicionar)
    entry_valor = tk.Entry(janela_adicionar)
    entry_descricao = tk.Entry(janela_adicionar)
    
    entry_data.grid(row=0, column=1, padx=10, pady=5)
    entry_valor.grid(row=1, column=1, padx=10, pady=5)
    entry_descricao.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Button(janela_adicionar, text="Adicionar", command=adicionar).grid(row=3, column=1, pady=10)

def adicionar_despesa_interface():
    def adicionar():
        data = entry_data.get()
        valor = float(entry_valor.get())
        descricao = entry_descricao.get()
        adicionar_despesa(data, valor, descricao)
        messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
        janela_adicionar.destroy()

    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Despesa")
    
    tk.Label(janela_adicionar, text="Data").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(janela_adicionar, text="Valor").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(janela_adicionar, text="Descrição").grid(row=2, column=0, padx=10, pady=5)
    
    entry_data = tk.Entry(janela_adicionar)
    entry_valor = tk.Entry(janela_adicionar)
    entry_descricao = tk.Entry(janela_adicionar)
    
    entry_data.grid(row=0, column=1, padx=10, pady=5)
    entry_valor.grid(row=1, column=1, padx=10, pady=5)
    entry_descricao.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Button(janela_adicionar, text="Adicionar", command=adicionar).grid(row=3, column=1, pady=10)

def deletar_receita_interface():
    def deletar():
        id_receita = entry_id.get()
        if not id_receita.isdigit():
            messagebox.showerror("Erro", "ID da receita deve ser um número inteiro.")
            return
        
        id_receita = int(id_receita)
        deletar_receita(id_receita)
        messagebox.showinfo("Sucesso", f"Receita com ID {id_receita} deletada com sucesso!")
        janela_deletar.destroy()

    janela_deletar = tk.Toplevel()
    janela_deletar.title("Deletar Receita")
    
    tk.Label(janela_deletar, text="ID da Receita").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(janela_deletar)
    entry_id.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Button(janela_deletar, text="Deletar", command=deletar).grid(row=1, column=0, columnspan=2, pady=10)

def deletar_despesa_interface():
    def deletar():
        id_despesa = entry_id.get()
        if not id_despesa.isdigit():
            messagebox.showerror("Erro", "ID da despesa deve ser um número inteiro.")
            return
        
        id_despesa = int(id_despesa)
        deletar_despesa(id_despesa)
        messagebox.showinfo("Sucesso", f"Despesa com ID {id_despesa} deletada com sucesso!")
        janela_deletar.destroy()

    janela_deletar = tk.Toplevel()
    janela_deletar.title("Deletar Despesa")
    
    tk.Label(janela_deletar, text="ID da Despesa").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(janela_deletar)
    entry_id.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Button(janela_deletar, text="Deletar", command=deletar).grid(row=1, column=0, columnspan=2, pady=10)

def visualizar_dados_interface():
    receitas = visualizar_receitas()
    despesas = visualizar_despesas()
    relatorio = gerar_relatorio()

    janela_visualizar = tk.Toplevel()
    janela_visualizar.title("Relatório Financeiro")
    
    # Título e tabela para Receitas
    frame_receitas = tk.Frame(janela_visualizar)
    frame_receitas.pack(pady=10)
    tk.Label(frame_receitas, text="Tabela de Receitas", font='bold').pack()
    
    tree_receitas = ttk.Treeview(frame_receitas, columns=("ID", "Data", "Valor", "Descrição"), show='headings')
    tree_receitas.heading("ID", text="ID")
    tree_receitas.heading("Data", text="Data")
    tree_receitas.heading("Valor", text="Valor")
    tree_receitas.heading("Descrição", text="Descrição")
    tree_receitas.column("ID", anchor="center")
    tree_receitas.column("Data", anchor="center")
    tree_receitas.column("Valor", anchor="center")
    tree_receitas.column("Descrição", anchor="center")
    tree_receitas.pack()
    
    for receita in receitas:
        tree_receitas.insert('', 'end', values=(receita[0], receita[1], receita[2], receita[3]))
    
    # Título e tabela para Despesas
    frame_despesas = tk.Frame(janela_visualizar)
    frame_despesas.pack(pady=10)
    tk.Label(frame_despesas, text="Tabela de Despesas", font='bold').pack()
    
    tree_despesas = ttk.Treeview(frame_despesas, columns=("ID", "Data", "Valor", "Descrição"), show='headings')
    tree_despesas.heading("ID", text="ID")
    tree_despesas.heading("Data", text="Data")
    tree_despesas.heading("Valor", text="Valor")
    tree_despesas.heading("Descrição", text="Descrição")
    tree_despesas.column("ID", anchor="center")
    tree_despesas.column("Data", anchor="center")
    tree_despesas.column("Valor", anchor="center")
    tree_despesas.column("Descrição", anchor="center")
    tree_despesas.pack()
    
    for despesa in despesas:
        tree_despesas.insert('', 'end', values=(despesa[0], despesa[1], despesa[2], despesa[3]))
    
    # Relatório Financeiro
    frame_relatorio = tk.Frame(janela_visualizar)
    frame_relatorio.pack(pady=10)
    
    tk.Label(frame_relatorio, text=f"Total de Receitas: {relatorio['Total de Receitas']}", fg='blue', font='bold').pack()
    tk.Label(frame_relatorio, text=f"Total de Despesas: {relatorio['Total de Despesas']}", fg='red', font='bold').pack()
    tk.Label(frame_relatorio, text=f"Saldo Final: {relatorio['Saldo Final']}", fg='green', font='bold').pack()


def criar_menu():
    janela_principal = tk.Tk()
    janela_principal.title("Controle Financeiro")
    
    frame_botoes = tk.Frame(janela_principal)
    frame_botoes.pack(pady=10)
    
    btn_adicionar_receita = tk.Button(frame_botoes, text="Adicionar Receita", command=adicionar_receita_interface)
    btn_adicionar_receita.grid(row=0, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    
    btn_adicionar_despesa = tk.Button(frame_botoes, text="Adicionar Despesa", command=adicionar_despesa_interface)
    btn_adicionar_despesa.grid(row=0, column=1, padx=10, pady=5, ipadx=10, ipady=5)
    
    btn_deletar_receita = tk.Button(frame_botoes, text="Deletar Receita", command=deletar_receita_interface)
    btn_deletar_receita.grid(row=0, column=2, padx=10, pady=5, ipadx=10, ipady=5)
    
    btn_deletar_despesa = tk.Button(frame_botoes, text="Deletar Despesa", command=deletar_despesa_interface)
    btn_deletar_despesa.grid(row=0, column=3, padx=10, pady=5, ipadx=10, ipady=5)
    
    btn_visualizar = tk.Button(frame_botoes, text="Visualizar Dados", command=visualizar_dados_interface)
    btn_visualizar.grid(row=0, column=4, padx=10, pady=5, ipadx=10, ipady=5)

    janela_principal.mainloop()

if __name__ == "__main__":
    criar_menu()
