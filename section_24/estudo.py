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


class MinhaTela(BoxLayout):

    def click(self):
        print("oi")

class Estudo4App(App):
    pass

janela = Estudo4App()
janela.run()