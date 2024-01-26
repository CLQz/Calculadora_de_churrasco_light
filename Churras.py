from tkinter import *
import pandas as pd

# Importando base de dados com os valores
val = pd.read_csv("valores.csv", encoding="utf-8", index_col=0)

# Função que calcula o resultado final a ser arrecadado
def calculadora():
    spin2.config(to=var.get())
    spin3.config(to=var.get())
    c = (var.get() * (val["Dieta"][0] + val["Alcool"][0])) + \
        (var2.get() * (val["Dieta"][1] - val["Dieta"][0])) + \
        (var3.get() * (val["Alcool"][1] - val["Alcool"][0]))
    res_lab.config(text=f"Total a arrecadar: {str(c)} reais.")

# Função que cria a janela de mudança de valores utilizados no calculo
def janela_configuracao():
    # Criação da janela
    janela2 = Toplevel(bg="white")
    janela2.title("Edição de parâmetros")
    janela2.resizable(False, False)
    # Ligando Clicks, Tecla Tab e Tecla Enter a Função editor_valores
    janela2.bind("<Return>", lambda x: editor_valores(v.get(), v2.get(), v3.get(), v4.get()))
    janela2.bind("<Tab>", lambda x: editor_valores(v.get(), v2.get(), v3.get(), v4.get()))
    janela2.bind("<Enter>", lambda x: editor_valores(v.get(), v2.get(), v3.get(), v4.get()))
    # Criação dos textos e caixas que informam o valor atual e a seleção de valores novos
    mud = Label(janela2, text="Valor Com Alcool:", bg="white")
    mud.place(relx=0.15, rely=0.1)
    v = IntVar()
    v.set(val["Alcool"][0])
    chng_box1 = Spinbox(janela2, width=4, from_=0, to=200, textvariable=v,
                        command=lambda: editor_valores(v.get(), v2.get(), v3.get(), v4.get()))
    chng_box1.place(relx=0.65, rely=0.1)
    mud2 = Label(janela2, text="Valor Sem Alcool:", bg="white")
    mud2.place(relx=0.15, rely=0.3)
    v2 = IntVar()
    v2.set(val["Alcool"][1])
    chng_box2 = Spinbox(janela2, width=4, from_=0, to=200, textvariable=v2,
                        command=lambda: editor_valores(v.get(), v2.get(), v3.get(), v4.get()))
    chng_box2.place(relx=0.65, rely=0.3)
    mud3 = Label(janela2, text="Valor Com Carne:", bg="white")
    mud3.place(relx=0.15, rely=0.5)
    v3 = IntVar()
    v3.set(val["Dieta"][0])
    chng_box3 = Spinbox(janela2, width=4, from_=0, to=200, textvariable=v3,
                        command=lambda: editor_valores(v.get(), v2.get(), v3.get(), v4.get()))
    chng_box3.place(relx=0.65, rely=0.5)
    mud4 = Label(janela2, text="Valor Sem Carne:", bg="white")
    mud4.place(relx=0.15, rely=0.7)
    v4 = IntVar()
    v4.set(val["Dieta"][1])
    chng_box4 = Spinbox(janela2, width=4, from_=0, to=200, textvariable=v4,
                        command=lambda: editor_valores(v.get(), v2.get(), v3.get(), v4.get()))
    chng_box4.place(relx=0.65, rely=0.7)

# Função que muda os valores utilizados e os salva sobrescrevendo a planilha
def editor_valores(v, v2, v3, v4):
    val["Alcool"][0] = v
    val["Alcool"][1] = v2
    val["Dieta"][0] = v3
    val["Dieta"][1] = v4
    val.to_csv("valores.csv", encoding="utf-8")
    calculadora()

# Criando janela principal
janela = Tk()
janela.resizable(False, False)
janela.title("Calculadora de churrasco light")
janela.geometry("560x183+300+160")
# Ligando Clicks, Tecla Tab e Tecla Enter a Função Calculadora
janela.bind("<Return>", lambda x: calculadora())
janela.bind("<Tab>", lambda x: calculadora())
janela.bind("<Enter>", lambda x: calculadora())

# Criando frame de entrada de numero de convidados
conv = Frame(janela, width=190, height=125, bg="#E5013A")
conv.grid(row=0, column=0, sticky=N)
cn_lab = Label(conv, text="Quantas pessoas\nvão no churrasco?", font="Ivy 14 italic", bg='#E5013A')
cn_lab.place(x=10, y=12)
var = IntVar()
var.set(8)
spin1 = Spinbox(conv, width=5, from_=1, to=500, command=calculadora, textvariable=var)
spin1.place(x=67, y=88)

# Criando frame de entrada de numero de veganos
comida = Frame(janela, width=185, height=125, bg="#E5013A")
comida.grid(row=0, column=1)
co_lab = Label(comida, text="Quantos pessoas\nnão comem carne?", font="Ivy 14 italic", bg='#E5013A')
co_lab.place(x=10, y=12)
var2 = IntVar()
spin2 = Spinbox(comida, width=5, from_=0, to=var.get(), textvariable=var2, command=calculadora)
spin2.place(x=67, y=88)

# Criando frame de entrada de numero de pessoas que nao bebem
bebida = Frame(janela, width=185, height=125, bg="#E5013A")
bebida.grid(row=0, column=2)
be_lab = Label(bebida, text="Quantas pessoas\n não bebem?", font="Ivy 14 italic", bg='#E5013A')
be_lab.place(x=10, y=12)
var3 = IntVar()
spin3 = Spinbox(bebida, width=5, from_=0, to=var.get(), textvariable=var3, command=calculadora)
spin3.place(x=67, y=88)

# Criando frame de saida dos resultados
res = Frame(janela, width=560, height=58, bg="#E5013A")
res.grid(row=1, column=0, columnspan=3)
res_lab = Label(res, text="Total a arrecadar:  reais.", font="Ivy 14 italic", bg='#E5013A')
calculadora()
res_lab.place(x=10, y=12)

# Criando botao de edicao de parametros e colocando no frame dos resultados
icon2 = PhotoImage(file="engrenagem.png")
editor = Button(res, text="click", image=icon2, command=janela_configuracao,
                bg='#E5013A', relief="flat", activebackground="#E5013A")
editor.place(in_=res, relx=0.92, rely=0.15)

janela.mainloop()
