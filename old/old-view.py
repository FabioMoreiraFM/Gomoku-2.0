# encoding: utf-8
from jogador import *

class View:
	def __init__(self):
		return

	def exibir_tabuleiro(self, tabuleiro):
		tamanho = len(tabuleiro)
		linha = ''
		print '######TABULEIRO ATUAL########'
		for y in range(tamanho-1):
			for x in range(tamanho-1):
				linha += str(tabuleiro[x][y].get_dono().value) + ' '	
			print linha
			linha = ''

	def tamanho_tabuleiro(self):
		try:
			return int(raw_input("Qual o tamanho do tabuleiro? "))
		except ValueError:
			print "Insira um número válido"
			return self.tamanho_tabuleiro()

	def escolha_posicao_inserir_peca(self):
		return [int(y) for y in raw_input("Escolha a coordenada para inserir a peça: ").split()]

	def mensagem_fim_de_jogo(self, jogador_atual):
		print "Parabéns " + str(jogador_atual) + ", você ganhou"

	def opcao_jogo(self):
		try:
			return int(raw_input("Partida HxIA (0) - Partida HxH (1): "))
		except ValueError:
			print "Insira um número válido"
			return self.opcao_jogo()

	def exibir_encadeamento(self, encadeamento):
		print str(encadeamento[Jogador.ADVERSARIO_1]) + "    "+ str(encadeamento[Jogador.ADVERSARIO_2])

	def msg_erro_inserir_peca(self):
		print "Jogada inválida, tente novamente"