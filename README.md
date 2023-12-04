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
- - o uso do __ ante da variável, indica as compilador que ela não pode ser acessada diretamente.
Exemplo:
```python
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
```
