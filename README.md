# applications-with-kivy-in-python
- Repositório para o curso da framework kivy do python
- Desenvolvimento de Apps Comerciais com Python e Kivy para Android, iOS,

## para uso
* intale as dependências dos requerimentos
```shell
pip install -r requirement.txt
```
- [x] [Manual em português do kivy](kivy-pt_br-excript.pdf)

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


#### ```@property com @metodo.setter```
Exemplo
```Python
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
```
## Classe em Python
- As classe são utilizadas para criar objetos e em __Python__ as mesmas também são objetos.
- Cuidado com as nomenclatura:
- [x] MEMBROS DE CLASSE
- [x] MEMBROS DE INSTÂNCIAS
- Aprenderemos a operar um membro de classe.

* Ao operar as classes, altera-se todos os membros juntos, se alterar apenas o membro será alterado apenas no referido.
* Na busca por atributos o __Python__, irá busca primeiro na membro atributo, caso não encontre ele busca na classe.


- Exemplo de Método de classe:
```python
class A:
  #Todas as instancias possuem acesso
  @classmethod
  def fun(cls, arg1, arg2, ...):
    pass #Informa que não irei implementar por enquanto

```
## Método Estáticos
- Não possui relação direta com a classe, porém são membro de classe. sem a declaração de parâmetros "cls" ou "self"
## Posicionamento
- A biblioteca __Kivy__ opera no primeiro plano cartesiano.
- o Posicionamento se baseia-se no ângulo inferior esquerdo, para início do posicionamento.
- É de responsabilidade do programador posicionar as janelas, caso contrario, não será exibido na tela
- Sistemas de medidas responsivo.
- Definir de forma automática com consequência a resolução das telas(pixel).
- dp, independa do tamanho da tela é proporcional a largura de pixel pela densidade da tela.
![dp](figure/dp.png)

## Tela com algumas funcionalidades da biblioteca __kivy__
- A aplicação permite apenas um widget's principal, porém, cria-se leiautes para várias janelas.
```python
from kivy.app import App
from kivy.uix.label import Label          #Escrita de texto
from kivy.uix.button import Button        #Botão
from kivy.uix.textinput import TextInput  #Entrada de texto

```




# Linguagem __Kivy__

```python
<ClassName>: #É o top da janela, (Haverá uma única janela, pois os dispositivos moveis usam apenas uma janela)
  LayoutType: #Gerenciador de Layout
    WidgetType: # Widget (Terá vários)
      pos: 10, 10
      size: .5, .5

  LayoutType2: #Gerenciador de Layout generico
      font_size: 70
      center_x: root.width / 4
      top: root.top - 5
      text: "0"

```
## Propriedades Percentuais

![Propriedade de posição](figure/prp.png)


## Para testes de tela em diversas telas de aparelhos movéis :D

```sheel
activate k35 #Ativa o ambiente virtual do python 3.5

#Vá no diretório da aplicação
dir "caminho_path_app"

python nome_app.py -m screen #Lista os dispositivos suportados

pyhton nome_app.py -m screen:nome_dispositivo
```

### ipython
- Roda em linha de comando e interage em diversas outros scripty

```shell
cd dir_app

jupyter notebook #Abre o jupyter no navegador padrão

```
## kivy


- MinhaApp - minha.kv
- ProgramaApp - programa.kv
- Prog - prog.kv


## Palavras reservadas em Kivy

![Palavras Reservadas](figure/reservadas.png)



```kivy
<Class>:
    Label:
        text: str(self.opacity) # Aponta para



<Classe>:
    Label:
      #root = <Classe> Aponta para a classe implementada pelo pyhton
      text:root.orientation


###############################
<Class>:
    Label:
        app.name
```

## Widget ![wd](figure/wid.png)



<div id="js-clones-graph" data-target="traffic-clones-graph.container" data-view-component="true" class="Box Box--condensed mb-4">
  <div id="header-53ab21ec-1d46-4ef7-9b3e-fe9611db72a4" data-view-component="true" class="Box-header">
  <h3 data-view-component="true" class="Box-title">          Git clones
</h3>

</div>

    <ul aria-labelledby="header-53ab21ec-1d46-4ef7-9b3e-fe9611db72a4" data-view-component="true">
        <li data-view-component="true" class="Box-row">        <div class="graph-canvas traffic-graph uniques-graph js-graph" data-url="/OgliariNatan/applications-with-kivy-in-python/graphs/clone-activity-data" data-target="traffic-clones-graph.graph">
          <div class="activity">
  <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="graph-loading dots mb-2 anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>
  <div class="graph-loading msg">
    <p>Crunching the latest data, just for you. Hang tight…</p>
  </div>
  <div class="graph-empty msg mt-6">
    <h3>We don’t have enough data to show anything useful.</h3>
    <p>It usually takes about a week to populate this graph.</p>
  </div>
  <div class="graph-too-large msg mt-6">
    <h3>There are too many commits to generate this graph.</h3>
    <p>More information about this data can be found in the
      <a class="Link--inTextBlock" href="https://docs.github.com/repositories/viewing-activity-and-data-for-your-repository/analyzing-changes-to-a-repositorys-content">activity documentation</a>.
    </p>
  </div>
  <div class="graph-no-usable-data msg mt-6">
    <p>We need at least one non-empty commit with an email to generate this graph.</p>
  </div>
</div>

<div data-view-component="true" class="graph-error flash flash-error m-3">

  <p>We tried our best, but the graph wouldn’t load. Try reloading the page.</p>



</div>
        <svg viewBox="0 0 719 243" preserveAspectRatio="xMinYMin meet" class="viz" data-hpc=""><g transform="translate(40,20)"><g class="x axis" fill="none" font-size="10" font-family="sans-serif" text-anchor="middle"><path class="domain" stroke="currentColor" d="M0.5,198V0.5H639.5V198"></path><g class="tick" opacity="1" transform="translate(0.5,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/01</text></g><g class="tick" opacity="1" transform="translate(49.65384615384615,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/02</text></g><g class="tick" opacity="1" transform="translate(98.8076923076923,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/03</text></g><g class="tick" opacity="1" transform="translate(147.96153846153848,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/04</text></g><g class="tick" opacity="1" transform="translate(197.1153846153846,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/05</text></g><g class="tick" opacity="1" transform="translate(246.26923076923077,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/06</text></g><g class="tick" opacity="1" transform="translate(295.42307692307696,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/07</text></g><g class="tick" opacity="1" transform="translate(344.57692307692304,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/08</text></g><g class="tick" opacity="1" transform="translate(393.7307692307692,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/09</text></g><g class="tick" opacity="1" transform="translate(442.88461538461536,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/10</text></g><g class="tick" opacity="1" transform="translate(492.03846153846155,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/11</text></g><g class="tick" opacity="1" transform="translate(541.1923076923077,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/12</text></g><g class="tick" opacity="1" transform="translate(590.3461538461539,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/13</text></g><g class="tick" opacity="1" transform="translate(639.5,0)"><line stroke="currentColor" y2="198"></line><text fill="currentColor" y="208" dy="0.71em">12/14</text></g></g><g class="y axis views" fill="none" font-size="10" font-family="sans-serif" text-anchor="end"><path class="domain" stroke="currentColor" d="M-6,193.5H0.5V0.5H-6"></path><g class="tick" opacity="1" transform="translate(0,193.5)"><line stroke="currentColor" x2="-6"></line><text fill="currentColor" x="-9" dy="0.32em">0</text></g><g class="tick" opacity="1" transform="translate(0,116.3)"><line stroke="currentColor" x2="-6"></line><text fill="currentColor" x="-9" dy="0.32em">10</text></g><g class="tick" opacity="1" transform="translate(0,39.099999999999994)"><line stroke="currentColor" x2="-6"></line><text fill="currentColor" x="-9" dy="0.32em">20</text></g></g><path class="path total" d="M0,0L49.15384615384615,193L98.3076923076923,193L147.46153846153848,108.08000000000001L196.6153846153846,131.23999999999998L245.76923076923077,123.52L294.92307692307696,123.52L344.07692307692304,169.84L393.2307692307692,193L442.38461538461536,185.28L491.53846153846155,154.4L540.6923076923077,138.96L589.8461538461539,146.68L639,193"></path><path class="path unique" d="M0,32.16666666666666L49.15384615384615,193L98.3076923076923,193L147.46153846153848,136.70833333333331L196.6153846153846,136.70833333333331L245.76923076923077,136.70833333333331L294.92307692307696,152.79166666666666L344.07692307692304,168.875L393.2307692307692,193L442.38461538461536,184.95833333333334L491.53846153846155,160.83333333333334L540.6923076923077,144.75L589.8461538461539,160.83333333333334L639,193"></path><g class="dots totals"><circle cx="0" cy="0" r="4"></circle><circle cx="49.15384615384615" cy="193" r="4"></circle><circle cx="98.3076923076923" cy="193" r="4"></circle><circle cx="147.46153846153848" cy="108.08000000000001" r="4"></circle><circle cx="196.6153846153846" cy="131.23999999999998" r="4"></circle><circle cx="245.76923076923077" cy="123.52" r="4"></circle><circle cx="294.92307692307696" cy="123.52" r="4"></circle><circle cx="344.07692307692304" cy="169.84" r="4"></circle><circle cx="393.2307692307692" cy="193" r="4"></circle><circle cx="442.38461538461536" cy="185.28" r="4"></circle><circle cx="491.53846153846155" cy="154.4" r="4"></circle><circle cx="540.6923076923077" cy="138.96" r="4"></circle><circle cx="589.8461538461539" cy="146.68" r="4"></circle><circle cx="639" cy="193" r="4"></circle></g><g class="dots uniques"><circle cx="0" cy="32.16666666666666" r="4"></circle><circle cx="49.15384615384615" cy="193" r="4"></circle><circle cx="98.3076923076923" cy="193" r="4"></circle><circle cx="147.46153846153848" cy="136.70833333333331" r="4"></circle><circle cx="196.6153846153846" cy="136.70833333333331" r="4"></circle><circle cx="245.76923076923077" cy="136.70833333333331" r="4"></circle><circle cx="294.92307692307696" cy="152.79166666666666" r="4"></circle><circle cx="344.07692307692304" cy="168.875" r="4"></circle><circle cx="393.2307692307692" cy="193" r="4"></circle><circle cx="442.38461538461536" cy="184.95833333333334" r="4"></circle><circle cx="491.53846153846155" cy="160.83333333333334" r="4"></circle><circle cx="540.6923076923077" cy="144.75" r="4"></circle><circle cx="589.8461538461539" cy="160.83333333333334" r="4"></circle><circle cx="639" cy="193" r="4"></circle></g><g class="y axis unique" transform="translate(639, 0)" fill="none" font-size="10" font-family="sans-serif" text-anchor="start"><path class="domain" stroke="currentColor" d="M6,193.5H0.5V0.5H6"></path><g class="tick" opacity="1" transform="translate(0,193.5)"><line stroke="currentColor" x2="6"></line><text fill="currentColor" x="9" dy="0.32em">0</text></g><g class="tick" opacity="1" transform="translate(0,113.08333333333331)"><line stroke="currentColor" x2="6"></line><text fill="currentColor" x="9" dy="0.32em">10</text></g><g class="tick" opacity="1" transform="translate(0,32.66666666666666)"><line stroke="currentColor" x2="6"></line><text fill="currentColor" x="9" dy="0.32em">20</text></g></g><rect class="overlay" width="639" height="193"></rect></g></svg></div>
</li>
        <li data-view-component="true" class="Box-row">        <div class="traffic-graph-stats">
          <ul class="summary-stats">
            <li class="p-2">
              <span class="num js-traffic-total clones">84</span>
              Clones
            </li>
            <li class="p-2">
              <span class="num js-traffic-uniques uniques">30</span>
              Unique cloners
            </li>
          </ul>
        </div>
</li>
</ul>  
</div>
