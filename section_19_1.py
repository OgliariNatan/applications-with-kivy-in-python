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



#class MinhaClasse:

#    membro_cls = 50 #Pode ser declarado em qualque parte no escopo da classe

#    def __init__(self): #Membro de instancia
#       self.mebro_inst =

#   def func(self):
#       print('o metodo func() foi invocado')
#       print(self.mebro_inst)
#       print(self.membro_cls)
#       print(MinhaClasse.membro_cls)

#i1 = MinhaClasse()
#i2 = MinhaClasse()

#print(MinhaClasse.membro_cls)
#print(i1.membro_cls)
#print(i2.membro_cls)
#print("-----inicio--------")

#i1.membro_cls = 1000
#print(MinhaClasse.membro_cls)
#print(i1.membro_cls)
#print(i2.membro_cls)

#print("----FIM------")

#i1.mebro_inst = 10
#print('i1: ' + str(i1.mebro_inst))
#print('i2: ' + str(i2.mebro_inst))
#MinhaClasse.membro_cls = 9

#print("---------------------")

#print('i1: ' + str(i1.membro_cls))
#print('i2: ' + str(i2.membro_cls))


class AAA:
    pass

bbb = AAA()

AAA.var_cls = "AAA.var_cls"
bbb.var_inst = "bbb.var_inst"

bbb.var_cls = "bbb.var_cls"

print(AAA.var_cls)
print(bbb.var_inst)
print(bbb.var_cls)

