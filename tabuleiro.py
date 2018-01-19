# encoding: utf-8
import nodo
from jogador import *

class Tabuleiro:

	_tabuleiro = None
	_nodos_disponiveis = None

	def __init__(self, tamanho):
		self._tabuleiro = [[nodo.Nodo([x,y], Jogador.ESPACO_LIVRE) for y in range(tamanho+1)] for x in range(tamanho+1)] 
		self._nodos_disponiveis = {}
		self._criar_dict_nodos_disponiveis(tamanho)

	def _criar_dict_nodos_disponiveis(self, tamanho):
		for x in range(tamanho):
			for y in range(tamanho):
				self._nodos_disponiveis[(x,y)] = self._tabuleiro[x][y]
	
	def inserir_peca(self, coordenada, novo_dono):
		nodo = self._tabuleiro[coordenada[0]][coordenada[1]]
		
		if (nodo.get_dono() == Jogador.ESPACO_LIVRE):
			nodo.set_dono(novo_dono)
			del self._nodos_disponiveis[(coordenada[0],coordenada[1])]
		else:
			raise Exception('Você adicionou uma peça inválida')

	def remover_peca(self, nodo):
		nodo.set_dono(Jogador.ESPACO_LIVRE)
		self._nodos_disponiveis[(nodo.get_coordenada()[0], nodo.get_coordenada()[1])] = nodo	

	def get_nodos_disponiveis(self):
		return self._nodos_disponiveis

	def get_tabuleiro(self):
		return self._tabuleiro