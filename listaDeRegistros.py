"Exercício de programação orientada a objetos em Python (versão 3.7)"
class BancoDeDados:
	def __init__(self, *registros, nome=None, idade=None, sexo=None, nacionalidade=None):
		'''Esse método colhe informações inseridas aos parametros, e as armazena em um argumento lista de nome "registro".
		
		"param" registro: list
		"param" nome: string
		"param" idade: integer
		"param" sexo: string
		"param" nacionalidade: string
		'''
		self.nome = nome
		self.idade = idade
		self.sexo = sexo
		self.nacionalidade = nacionalidade
		self.registros = list(registros)
		
if __name__=='__main__':
	p1 = BancoDeDados(nome='Fulano', idade=20, sexo='Masculino', nacionalidade='Brasil')
	p2 = BancoDeDados(nome='Folana', idade=21, sexo='Feminino', nacionalidade='Argentina')
	p3 = BancoDeDados(nome='Siclano', idade=22, sexo='Masculino', nacionalidade='Chile')
	p4 = BancoDeDados(nome='Beltrana', idade=23, sexo='Feminino', nacionalidade='Colombia')
	p5 = BancoDeDados(nome='Beltrano', idade=23, sexo='Masculino', nacionalidade='Colombia')
	reg = BancoDeDados(p1, p2, p3, p4, p5)
	
	print('@ Banco de Dados:')
	print()
	
	for registro in reg.registros:
		print('Nome: {}\nIdade: {}\nSexo: {}\nNacionalidade: {}'.format(registro.nome, registro.idade, registro.sexo, registro.nacionalidade))
		print('<---------------------------------->')