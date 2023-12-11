#coding: utf-8
#####	NOME:				setion_22.py
#####	VERSÃO:				1.2
#####	DESCRIÇÃO:			Implementação dos exercícios do curso de kivy
#####	DATA DA CRIAÇÃO:	01/12/2023
#####   ATUALIZADO EM:      xx/xx/xxxxxx
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/OgliariNatan/applications-with-kivy-in-python


kv = """
<Inicio@StackLayout>:
    orientation: 'lr-tb'
    spacing: 5
    padding: 5

Inicio:

    Login:
        id: popup
        size_hint: 0.7, 0.4

<Login@Popup>:

    title: 'Login e Senha'
"""





import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window #Para alterar o tamanho da janela de aoplicação
from kivy.lang import Builder

class TelinhaApp(App):

    def build(self):
        return Builder.load_string(kv)

TelinhaApp().run()

