"Exercício de programação orientada a objetos em Python 3.7"

"""
Você deve criar uma classe carro que vai possuir dois atributos compostos
por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade. Ele oferece os
seguintes atributos:
1° Atributo de dado velocidade.
2° Método acelerar, que deverá incrementar a velocidade em uma unidade.
3° Método frear, que deverá decrementar a velocidade em duas unidades.

A Direção terá a responsabilidade de controlar a direção. Ela oferece os
seguintes atributos:
1° Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2° Método girar_a_direita, que mudará a direção do carro para a direita.
3° Método girar_a_esquerda, que mudará a direção do carro para a esquerda.

    Exemplo:
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> # Executando classe Carro e suas funcionalidades finais
    >>> carro = Carro()
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Oeste'
"""
class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
        else:
            pass

class Direcao:
    def __init__(self, i=0):
        self.valor = 'Norte'
        self.opcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
        self.i = i

    def girar_a_direita(self):
        self.i += 1
        if self.i > 3:
            self.i = 0
            self.valor = self.opcoes[self.i]
        else:
            self.valor = self.opcoes[self.i]

    def girar_a_esquerda(self):
        self.i -= 1
        if self.i < -3:
            self.i = 0
            self.valor = self.opcoes[self.i]
        else:
            self.valor = self.opcoes[self.i]

class Carro:
    def __init__(self, motor=Motor(), direcao=Direcao()):
        self.motor = motor
        self.direcao = direcao

    def acelerar(self):
        self.acelerador = self.motor.acelerar()

    def frear(self):
        self.freio = self.motor.frear()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar_a_direita(self):
        self.volante = self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.volante = self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.valor