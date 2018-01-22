from jogador import *
import math
import controleEncadeamento
import copy

class IA:
	_controle_encadeamento = None
	_tabuleiro = None
	_melhor_jogada = None

	def __init__(self, controleEncadeamento):
		self._controle_encadeamento = controleEncadeamento

	def set_tabuleiro(self, tabuleiro):
		self._tabuleiro = tabuleiro

	def fim_de_jogo(self, encadeamento): 
		if encadeamento[Jogador.ADVERSARIO_1][4] >= 1:
			return False
		elif encadeamento[Jogador.ADVERSARIO_2][4] >= 1:
			return False
		else:
			return True

	def heuristica(self, jogador):

		if not(self.fim_de_jogo(self._controle_encadeamento.get_encadeamento())) and jogador:
			return -float('inf')

		if not(self.fim_de_jogo(self._controle_encadeamento.get_encadeamento())) and not(jogador):
			return float('inf')

		somatorioComputador = 0
		somatorioJogador = 0
		encadeamento_atual = self._controle_encadeamento.get_encadeamento()

		for i in range(0, len(encadeamento_atual[Jogador.ADVERSARIO_1])):
			somatorioJogador += encadeamento_atual[Jogador.ADVERSARIO_1][i]*(i**4)

		for i in range(0, len(encadeamento_atual[Jogador.ADVERSARIO_2])):
			somatorioComputador += encadeamento_atual[Jogador.ADVERSARIO_2][i]*(i**4)

		return somatorioComputador - somatorioJogador		

	def minimax(self, profundidade, alpha=-float('inf'), beta=float('inf'), mini_max=True):
		if profundidade == 0:
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
		
		if mini_max:
			return alpha
		else:
			return beta

	def melhor_jogada(self):
		return self._melhor_jogada