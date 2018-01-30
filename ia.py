from Model.jogador import *
import math
import Model.controleEncadeamento
import copy

class IA:
	_controle_encadeamento = None
	_tabuleiro = None
	_melhor_jogada = None

	def __init__(self, controleEncadeamento):
		self._controle_encadeamento = controleEncadeamento

	def set_tabuleiro(self, tabuleiro):
		self._tabuleiro = tabuleiro

	def heuristica(self, jogador):
		if self._controle_encadeamento.fim_de_jogo() and jogador:
			return -float('inf')

		if self._controle_encadeamento.fim_de_jogo() and not(jogador):
			return float('inf')

		somatorioComputador = 0
		somatorioJogador = 0
		encadeamento_atual = self._controle_encadeamento.get_encadeamento()

		for i in range(0, len(encadeamento_atual[Jogador.ADVERSARIO_1])):
			somatorioJogador += encadeamento_atual[Jogador.ADVERSARIO_1][i]*(i**4)
			somatorioComputador += encadeamento_atual[Jogador.ADVERSARIO_2][i]*(i**4)

		return somatorioComputador - somatorioJogador		

	def minimax(self, profundidade, alpha=-float('inf'), beta=float('inf'), mini_max=True):
		if profundidade == 0 or len(self._tabuleiro.get_nodos_disponiveis().keys()) == 0:
			return self.heuristica(mini_max)
		
		for tupla_coord in self._tabuleiro.get_nodos_disponiveis():
			index_coord = [tupla_coord[0], tupla_coord[1]]
			copia_encadeamento = copy.deepcopy(self._controle_encadeamento.get_encadeamento())
			
			if mini_max: #No futuro, colocar o que esta dentro do if/else em um metodo, o codigo eh igual
				self._tabuleiro.inserir_peca(index_coord , Jogador.ADVERSARIO_2) 
				self._controle_encadeamento.atualiza(index_coord)

				tmpalpha = self.minimax(profundidade-1, alpha, beta, False)
				
				if alpha < tmpalpha:
					alpha = tmpalpha
					self._melhor_jogada = index_coord 

				self._tabuleiro.remover_peca(self._tabuleiro.get_tabuleiro()[index_coord[0]][index_coord[1]])
				self._controle_encadeamento.set_encadeamento(copia_encadeamento)

				if beta <= alpha:
					break
			else:
				self._tabuleiro.inserir_peca(index_coord, Jogador.ADVERSARIO_1)
				self._controle_encadeamento.atualiza(index_coord)

				tmpbeta = self.minimax(profundidade-1, alpha, beta, True)
				
				if beta > tmpbeta:
					beta = tmpbeta

				self._tabuleiro.remover_peca(self._tabuleiro.get_tabuleiro()[index_coord[0]][index_coord[1]])
				self._controle_encadeamento.set_encadeamento(copia_encadeamento)

				if beta <= alpha:
					break
		
		return alpha if mini_max else beta

	def melhor_jogada(self):
		return self._melhor_jogada