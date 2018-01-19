from jogador import *
from orientacao import *

class ControleEncadeamento():
	_encadeamento = None
	_contador_incrementa_encadeamento = 0
	_jogador = None

	def __init__(self):
		self._encadeamento = {Jogador.ADVERSARIO_1: [0,0,0,0,0], Jogador.ADVERSARIO_2: [0,0,0,0,0]}

	def get_encadeamento(self):
		return self._encadeamento

	def atualiza(self, tabuleiro, coord_novo_nodo): # Tirar param tabuleiro dos metodos e colocar como var global
		self._jogador = tabuleiro[coord_novo_nodo[0]][coord_novo_nodo[1]].get_dono()
		encadeamento_unico = 0
		contador_orientacao = 0

		for orientacao in Orientacao:
			self.verifica_encadeamento(tabuleiro, coord_novo_nodo, orientacao)
			contador_orientacao += 1
			encadeamento_unico += self._contador_incrementa_encadeamento
			
			if contador_orientacao == 2: # Analisa o encadeamento depois de obter o resultado da Hori. Esq. + Hori. Dir., e.g.
				contador_orientacao = 0
				if self._contador_incrementa_encadeamento != 0:
					self._encadeamento[self._jogador][self._contador_incrementa_encadeamento] += 1
					self._contador_incrementa_encadeamento = 0
		
		if encadeamento_unico == 0:
			self._encadeamento[self._jogador][0] +=1 

	def verifica_encadeamento(self, tabuleiro, coord, orientacao):
		explora_vizinhaca_1 = coord[0] # x
		explora_vizinhaca_2 = coord[1] # y
		contador_vizinhos = -1 		   # -1 porque inicialmente o novo ponto incrementa o contador

		while tabuleiro[explora_vizinhaca_1][explora_vizinhaca_2].get_dono() == self._jogador :
			if orientacao == Orientacao.HORIZONTAL_ESQUERDA :
				explora_vizinhaca_1 -= 1
				explora_vizinhaca_2 += 0
			elif orientacao == Orientacao.HORIZONTAL_DIREITA :
				explora_vizinhaca_1 += 1
				explora_vizinhaca_2 += 0
			elif orientacao == Orientacao.VERTICAL_CIMA :
				explora_vizinhaca_1 += 0
				explora_vizinhaca_2 += 1
			elif orientacao == Orientacao.VERTICAL_BAIXO :
				explora_vizinhaca_1 += 0
				explora_vizinhaca_2 -= 1
			elif orientacao == Orientacao.DIAGONAL_PRINCIPAL_ESQUERDA :
				explora_vizinhaca_1 -= 1
				explora_vizinhaca_2 += 1
			elif orientacao == Orientacao.DIAGONAL_PRINCIPAL_DIREITA :
				explora_vizinhaca_1 += 1
				explora_vizinhaca_2 -= 1
			elif orientacao == Orientacao.DIAGONAL_SECUNDARIA_ESQUERDA :
				explora_vizinhaca_1 -= 1
				explora_vizinhaca_2 -= 1
			elif orientacao == Orientacao.DIAGONAL_SECUNDARIA_DIREITA :
				explora_vizinhaca_1 += 1
				explora_vizinhaca_2 += 1
			contador_vizinhos += 1

		if contador_vizinhos != 0 and self._encadeamento[self._jogador][contador_vizinhos-1] != 0:
		 	self._encadeamento[self._jogador][contador_vizinhos-1] -= 1
		self._contador_incrementa_encadeamento += contador_vizinhos

	def set_encadeamento(self, novo_encadeamento):
		self._encadeamento = novo_encadeamento