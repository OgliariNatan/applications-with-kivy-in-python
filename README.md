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
