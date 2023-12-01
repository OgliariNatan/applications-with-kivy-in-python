#####	NOME:				setion_19.py
#####	VERSÃO:				1.2
#####	DESCRIÇÃO:			Implementação dos exercícios do curso de kivy
#####	DATA DA CRIAÇÃO:	01/12/2023
#####   ATUALIZADO EM:      xx/xx/xxxxxx
#####	ESCRITO POR:		Natan Ogliari
#####	E-MAIL:				natanogliari@gmail.com
#####	LICENÇA:			MIT license
#####	PROJETO:			https://github.com/OgliariNatan/applications-with-kivy-in-python/tree/main


class Retangulo:

    def __init__(self, largura, altura):
        self.largura = 0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é inválida: {}".format(num))
        self.altura = num
    def set_largura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é inválida: {}".format(num))
        self.largura = num
    def get_area(self):
        return self.largura * self.altura




#r = Retangulo(largura=10, altura=5)
r = Retangulo(largura=1, altura=5)


print(r.get_area())