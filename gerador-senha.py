import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string
import random

def gerar_senha():
    try:
        comprimento = comprimento_var.get()
        incluir_maiusculas = maiusculas_var.get()
        incluir_numeros = numeros_var.get()
        incluir_especiais = especiais_var.get()

        caracteres = string.ascii_lowercase
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_especiais:
            caracteres += string.punctuation

        if not caracteres:
            mensagem_erro.config(text="Selecione pelo menos uma opção!")
            return
        else:
            mensagem_erro.config(text="")

        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        senha_var.set(senha)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def sair():
    janela.destroy()

def atualizar_label_comprimento(event=None):
    valor = int(comprimento_var.get())
    label_comprimento.config(text=f"Comprimento da Senha: {valor} caracteres")

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("500x430")
janela.resizable(True, True)

# Variáveis
comprimento_var = tk.IntVar(value=12)
maiusculas_var = tk.BooleanVar(value=True)
numeros_var = tk.BooleanVar(value=True)
especiais_var = tk.BooleanVar(value=True)
senha_var = tk.StringVar()

# Título
titulo = tk.Label(janela, text="Gerador de Senhas", font=('Helvetica', 24, 'bold'))
titulo.pack(pady=10)

# Slider de comprimento
frame_slider = tk.Frame(janela)
frame_slider.pack(pady=10)

label_comprimento = tk.Label(frame_slider, text=f"Comprimento da Senha: {comprimento_var.get()} caracteres", font=('Helvetica', 14))
label_comprimento.pack()

slider = ttk.Scale(frame_slider, from_=8, to=32, orient='horizontal', variable=comprimento_var, command=atualizar_label_comprimento)
slider.pack(fill='x', padx=20)

# Opções de caracteres
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack(pady=10)

tk.Checkbutton(frame_opcoes, text="Incluir letras maiúsculas", variable=maiusculas_var, font=('Helvetica', 12)).pack(anchor='w')
tk.Checkbutton(frame_opcoes, text="Incluir números", variable=numeros_var, font=('Helvetica', 12)).pack(anchor='w')
tk.Checkbutton(frame_opcoes, text="Incluir caracteres especiais", variable=especiais_var, font=('Helvetica', 12)).pack(anchor='w')

# Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_gerar = tk.Button(frame_botoes, text="Gerar Senha", font=('Helvetica', 14), bg='#46CC08', fg='white', command=gerar_senha)
btn_gerar.pack(side='left', padx=10)

btn_sair = tk.Button(frame_botoes, text="Sair", font=('Helvetica', 14), bg='#DC3545', fg='white', command=sair)
btn_sair.pack(side='left', padx=10)

# Campo de senha gerada
frame_senha = tk.Frame(janela)
frame_senha.pack(pady=10)

tk.Label(frame_senha, text="Senha gerada:", font=('Helvetica', 14)).pack()
entrada_senha = tk.Entry(frame_senha, textvariable=senha_var, font=('Helvetica', 14), width=35, state='readonly')
entrada_senha.pack()

# Mensagem de erro
mensagem_erro = tk.Label(janela, text="", font=('Helvetica', 12), fg='red')
mensagem_erro.pack(pady=5)

# Iniciar o programa
janela.mainloop()
