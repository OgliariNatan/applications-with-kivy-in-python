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
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

#App().run() #Gera uma janela em "branco"

# def click():
#     print("O botão foi clicado")
#
# def build():
#     #Para impressão de textos
#     lb = Label()
#     lb.text= "NATAN OGLIARI"
#     lb.italic=True
#     lb.font_size=50
#     # return lb
#
#     #para geração de botões
#     bt = Button()
#     bt.text="Clique Aqui"
#     bt.font_size=20
#     bt.on_press = click
#     #return bt
#
#     #texto de entrada
#     return TextInput(text="Componente entrada de texto")


# app = App()
# app.build = build
# app.run()


######################### PARA BAIXO



def build(): #Definição de componentes de tela
    layoute = FloatLayout() #Gerenciador de layoute

    ed = TextInput(text="Natan Ogliari") #Entrada de texto
    ed.size_hint = None, None #Redifine a posição do componente
    ed.height = 300
    ed.right = 400
    ed.x = 60
    ed.y = 250


    bt = Button(text="Clique aqui") # Adiciona botãoao layoute
    bt.size_hint = None, None #Redifine a posição do componente


    layoute.add_widget(ed) #Adiciona a instancia ao layoute
    layoute.add_widget(bt) #Adiciona a instancia ao layoute

    return layoute

janela = App()
janela.build = build
janela.run()