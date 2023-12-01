#coding: utf-8
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
        self._largura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
        self._altura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
        self.__var = 0
        self.set_altura(altura) #metodo acessor
        self.set_largura(largura) #metodo acessor

    def set_altura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é inválida: {}".format(num))
        self._altura = num
        self.__var = 456

    def set_largura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é inválida: {}".format(num))
        self._largura = num
    def get_area(self): #metodo de solicitação
        return self._largura * self._altura


#r = Retangulo(largura=10, altura=5)
r = Retangulo(largura=5, altura=5)

print(r.get_area())


print('----------------------------------------------')
print('NOVO METÓDO --- propriedade')


class A:
    def __init__(self):
        self._var = 0
    def _get_var(self):
        print("O valor está sendo lido")
        return self._var
    def _set_var(self, x):
        print("O valor está sendo escrito")
        self._var = x
    #Asociar a instancia ao metodo
    var = property(fget=_get_var, fset=_set_var)

a = A() #Instancia a class
a.var = 10
print(a.var)
print('________________________________________________________')
print('_______________DECOratORS_______________________')


class B:
    def __init__(self):
        self._var = 0
    @property
    def var(self):
        print("O valor está sendo lido")
        return self._var
    @var.setter
    def var(self, x):
        print("O valor está sendo escrito")
        self._var = x


b = B() #Instancia a class
b.var = 10
t = a.var

print(t)

