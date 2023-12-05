#coding: utf-8
#####	NOME:				setion_19.py
#####	VERSÃO:				1.2
#####	DESCRIÇÃO:			Implementação dos exercícios do curso de kivy
#####	DATA DA CRIAÇÃO:	01/12/2023
#####   ATUALIZADO EM:      xx/xx/xxxxxx
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/OgliariNatan/applications-with-kivy-in-python


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

#App().run() #Gera uma janela em "branco"

def click():
    print("O botão foi clicado")

def build(): #Para impressão de textos
    lb = Label()
    lb.text= "NATAN OGLIARI"
    lb.italic=True
    lb.font_size=50

    bt = Button()
    bt.text="Clique Aqui"
    bt.font_size=20
    bt.on_press = click

    return bt


app = App()
app.build = build
app.run()