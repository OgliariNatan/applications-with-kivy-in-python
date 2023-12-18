#coding: utf-8
#####	NOME:				setion_26.py
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
from kivy.uix.label import Label
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from tkinter import *
Window.clarcolor = get_color_from_hex("#FFFFFF")

#Força a aplicação a não iniciar em tela cheia
from kivy.config import Config
Config.set("graphics", "fullscreen", "0")

janela = None
glayout = None


class JanelaApp(App):
    pass

janela = JanelaApp()

kvcode = """

StackLayout:
    orientation: "tb-lr"
    padding: 50

"""

if(janela.root):
    janela.root_window.remove_widget( janela.root )
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string( kvcode )
janela.root_window.add_widget( glayout )
