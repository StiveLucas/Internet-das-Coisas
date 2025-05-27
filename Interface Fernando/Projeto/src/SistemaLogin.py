#Mecha e descubra o código abaixo para criar uma tela de login simples usando Tkinter.

# Importando a biblioteca Tkinter
from tkinter import *
from tkinter import messagebox

import banco

menuInicial = Tk()
menuInicial.title("Login")
menuInicial.geometry("400x200+500+170")
menuInicial.resizable(False, False)

Label1 = Label(menuInicial, text="Usuário", fg="black", font="Arial 12 bold")
Label1.grid(row=0, column=0, padx=0, pady=0)

Label2 = Label(menuInicial, text="Senha", fg="black", font="Arial 18 bold")
Label2.grid(row=1, column=0, padx=0, pady=0)

#Caixa de texto para o usuário
txtUsuario = Entry(menuInicial, width=30, font="Arial 12")
txtUsuario.grid(row=0, column=1, padx=0, pady=0)
txtUsuario.focus()

txtSenha = Entry(menuInicial, width=30, font="Arial 12")
txtSenha.grid(row=1, column=1, padx=0, pady=0)

#Botões
btLogin = Button(menuInicial, text="Login", width=10, font="Arial 15 bold", bg="green", fg="white")
btLogin.grid(row=2, column=1, padx=0, pady=10, sticky=W)

btCancelar = Button(menuInicial, text="Cancelar", width=10, font="Arial 15 bold", bg="red", fg="white")
btCancelar.grid(row=2, column=1, padx=0, pady=10, sticky=E)

#Funções

def cancelar():
    telaResposta = messagebox.askyesno("Cancelar", "Deseja realmente cancelar?")

    if telaResposta:
        menuInicial.destroy()

def login(): 
    nome = txtUsuario.get()
    senha = txtSenha.get()

    nome = nome.strip()
    senha = senha.strip()

    if nome == "" or senha == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    banco.salvar(nome, senha)

btLogin.config(command=login)
btCancelar.config(command=cancelar)



menuInicial.mainloop()