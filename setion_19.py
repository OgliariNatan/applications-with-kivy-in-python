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

#
# class Retangulo:
#
#     def __init__(self, largura, altura):
#         self._largura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
#         self._altura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
#         self.__var = 0
#         self._set_altura(altura) #metodo acessor
#         self._set_largura(largura) #metodo acessor
#
#     def _set_altura(self, num):
#         if(not(isinstance(num, int) and (num > 0))):
#             raise ValueError("Altura é inválida: {}".format(num))
#         self._altura = num
#         self.__var = 456
#
#     def _set_largura(self, num):
#         if(not(isinstance(num, int) and (num > 0))):
#             raise ValueError("Largura é inválida: {}".format(num))
#         self._largura = num
#     def _get_area(self): #metodo de solicitação
#         return self._largura * self._altura
#
#
# #r = Retangulo(largura=10, altura=5)
# r = Retangulo(largura=5, altura=5)
#
# print(r._get_area())
#
#
# print('----------------------------------------------')
# print('NOVO METÓDO --- propriedade')
#
#
# class A:
#     def __init__(self):
#         self._var = 0
#     def _get_var(self):
#         print("O valor está sendo lido")
#         return self._var
#     def _set_var(self, x):
#         print("O valor está sendo escrito")
#         self._var = x
#     #Asociar a instancia ao metodo
#     var = property(fget=_get_var, fset=_set_var)
#
# a = A() #Instancia a class
# a.var = 10
# print(a.var)
# print('________________________________________________________')
# print('_______________DECOratORS_______________________')
#
#
# class B:
#     def __init__(self):
#         self._var = 0
#     @property
#     def var(self):
#         print("O valor está sendo lido")
#         return self._var
#     @var.setter
#     def var(self, x):
#         print("O valor está sendo escrito")
#         self._var = x
#
#
# b = B() #Instancia a class
# b.var = 10
# t = a.var
#
# print(t)
#
# print('________________________________________________________')
# print('_______________DECORATORS_______________________')




#class Retangulo:

 #   def __init__(self, largura, altura):
  #      self._largura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
   #     self._altura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
    #    self._set_altura(altura) #metodo acessor
     #   self._set_largura(largura) #metodo acessor

  #  def _set_altura(self, num):
 #      if(not(isinstance(num, int) and (num > 0))):
#            raise ValueError("Altura é inválida: {}".format(num))
#       self._altura = num
#       self.__var = 456

#   def _set_largura(self, num):
#       if(not(isinstance(num, int) and (num > 0))):
#           raise ValueError("Largura é inválida: {}".format(num))
#       self._largura = num
#   def _get_area(self): #metodo de solicitação
#       return self._largura * self._altura
#   def _get_altura(self): #metodo de solicitação
#       return self._altura
#   def _get_largura(self): #metodo de solicitação
#       return self._largura


#    altura = property(fget=_get_altura,  fset=_set_altura)
#    largura = property(fget=_get_largura, fset=_set_largura)
#    area = property(fget=_get_area)

#r = Retangulo(altura=10, largura=5)
#r.largura = 5
#r.altura = 10
#print("valor da altura: ", r.altura)
#print('valor da largura: ', r.largura)
#print('valor de area: ', r.area)



class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
        self._altura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
        self.altura = altura #metodo acessor
        self.largura = largura #metodo acessor

    @property
    def altura(self): #metodo de solicitação
        return self._altura
    @altura.setter
    def altura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é inválida: {}".format(num))
        self._altura = num


    @property
    def largura(self): #metodo de solicitação
        return self._largura
    @largura.setter
    def largura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é inválida: {}".format(num))
        self._largura = num
    @property
    def area(self): #metodo de solicitação
        return self._largura * self._altura

r = Retangulo(altura=5, largura=5)
r.largura = 5
r.altura = 10
#r.area = 100 #Levanta um erro, pois é apenas captura de valor em vez de setar valor.
print("valor da altura: ", r.altura)
print('valor da largura: ', r.largura)
print('valor de area: ', r.area)