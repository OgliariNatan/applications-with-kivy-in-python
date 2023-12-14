#coding: utf-8
#####	NOME:				setion_24.py
#####	VERSÃO:				1.2
#####	DESCRIÇÃO:			Implementação dos exercícios do curso de kivy
#####	DATA DA CRIAÇÃO:	12/12/2023
#####   ATUALIZADO EM:      xx/xx/xxxxxx
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/OgliariNatan/applications-with-kivy-in-python
import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# class Estudo1App(App):
#     pass
#
# janela = Estudo1App()
# janela.run()


# class Estudo2App(App):
#     pass
#
# janela = Estudo2App()
# janela.run()

# class Estudo3App(App):
#     pass
#
# janela = Estudo3App()
# janela.run()

def funcSelf(x):
    print("FuncSelf")

Button.funcSelf = funcSelf


class MinhaTela(BoxLayout):

    def funcRoot(self):
        print("funcRoot")

class Estudo6App(App):
    def funcApp(self):
        print("funcApp")

janela = Estudo6App()
janela.run()