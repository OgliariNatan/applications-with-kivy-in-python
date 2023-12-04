# applications-with-kivy-in-python
- Repositório para o curso da framework kivy do python
- Desenvolvimento de Apps Comerciais com Python e Kivy para Android, iOS,

## para uso
* intale as dependências dos requerimentos
```shell
pip install -r requirement.txt
```

### Recursos interessante (Regras)
#### ```property```
- Nunca se acessa diretamente as variáveis.
- uso do ```property(fget= , fset= )``` </br>
- - ```var = property(fget=_get_var, fset=_set_var)```
- - o uso do __ ante da variável, indica as compilador que ela não pode ser acessada diretamente. </br>
Exemplo:
```python
class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
        self._altura = 0 #Não pode acessar diretamente, utilizar os metodos acessores
        self._set_altura(altura) #metodo acessor
        self._set_largura(largura) #metodo acessor

    def _set_altura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é inválida: {}".format(num))
        self._altura = num
        self.__var = 456

    def _set_largura(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é inválida: {}".format(num))
        self._largura = num
    def _get_area(self): #metodo de solicitação
        return self._largura * self._altura
    def _get_altura(self): #metodo de solicitação
        return self._altura
    def _get_largura(self): #metodo de solicitação
        return self._largura


    altura = property(fget=_get_altura,  fset=_set_altura)
    largura = property(fget=_get_largura, fset=_set_largura)
    area = property(fget=_get_area)

r = Retangulo(altura=10, largura=5)
r.largura = 50
r.altura = 10
print(r.altura)
print(r.largura)
print('valor de area')
print(r.area)
```
