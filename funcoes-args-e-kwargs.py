# O Python permite a utIlização de dois tipos de parâmetros
# "diferenciados" quando estamos declarando funções. São
# estes: *args e **kwargs.

# 1) *args
    # O parâmetro *args permite a manipulação de uma 
    # lista de argumentos (que não se sabe a quantidade
    # de itens) com uma única variável na declaração
    # da função. Exemplo:

    # Suponha que temos uma função simples que dê print
    # na lista de compras de uma pessoa:
    def lista_de_compras(pessoa, item1, item2, item3, item4):
        print(f'Lista de compras de {pessoa}:')
        print(item1)
        print(item2)
        print(item3)
        print(item4)

    # Se fôssemos usar a função para uma pessoa chamada
    # Juliana, seríamos obrigados a definir quatro
    # itens da lista de compra dela.
    lista_de_compras('Juliana', 'bananas', 'maçãs', 'macarrão', 'leite')

    # Mas e se houvesse uma pessoa cuja quantidade
    # de itens na lista de compras fosse maior do que quatro?
    # Ou menor do que quatro?

    # Nessa situação não conseguiríamos utilizar a função 
    # lista_de_compras. Seria necessário definir uma
    # outra função com mais do que quatro parâmetros
    # e uma outra com menos do que quatro parâmetros.
    # Isso tornaria o objetivo das funções (que é a de reutilizarmos
    # códigos) totalmente redundante. É nesse tipo de situação que 
    # utilizamos o parâmetro *args:
    def lista_de_compras(pessoa, *args):
        print(f'Lista de compras de {pessoa}:')
        for item in *args:
            print(item)

    # Com o parâmetro *args, não precisamos explicitamente
    # definir a quantidade de itens (ou parâmetros) que
    # utilizaremos em nossa função, mas é como se disséssemos
    # ao Python: "Python, estou declarando essa função,
    # mas não sei quantos itens a mais poderão ter, então salve
    # todos, independente de que seja 1 ou sejam 10, no parâmetro
    # *args". E assim podemos chamar a função lista_de_compras
    # da seguinte maneira, por exemplo:
    lista_de_compras('João', 'frango congelado', 'pães', 'sal de cozinha', 'leite')
    lista_de_compras('Maria', 'sacos de lixo')
    lista_de_compras('Bárbara', 'cenouras', 'abacate')

# 2) **kwargs
    # O parâmetro **kwargs tem uma função muito parecida
    # com a de *args. A diferença está em que: em *args,
    # passamos uma LISTA de valores, e por isso só podem
    # ser acessados através de uma iteração com "for",
    # por exemplo, acessando um a um através de seu índice.

    # Com **kwargs, supõe-se que, na chamada da função,
    # os argumentos "a mais", que não sabemos quantos são,
    # estejam sendo declarados na forma "chave=valor", ou
    # seja, como se fossem chaves/valores de um objeto.

    # Por exemplo, vamos declarar a função lista_de_compras
    # de forma que só seja possível ter um único "tipo" de
    # item na lista de compras:
    def lista_de_compras(pessoa, **kwargs):

        # Como **kwargs trata que os parâmetros sejam
        # como um objeto, podemos usar o método .get('chave')
        # do tipo de dado "objeto" para pegar o valor de uma
        # chave específica:
        fruta = kwargs.get('fruta')

        # Se, ao tentar pegar de kwargs, o valor da chave 'fruta'
        # não for None, signifca que então há uma chave chamada 
        # 'fruta', e que portanto há um valor para essa chave:
        if fruta is not None: 
            print(f'Na lista de compras há uma fruta: {fruta}')

    # Ao fazer a chamada da função, será da seguinte forma:
    lista_de_compras('Juliana', fruta='banana', massas='nhoque', verdura='alface')
    lista_de_compras('Cléber', bebida='guaraná', sorvete='flocos')
