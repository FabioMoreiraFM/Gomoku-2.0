from Model import model
from View import view
from Model.jogador import *

class Controller:
	_model = None
	_view = None
	_jogador_atual = Jogador.ADVERSARIO_2
	_tipo_partida = None
	_erro = False

	def __init__(self):
		self._model = model.Model()
		self._view = view.View(self)
		self._view.menu_inicial()

	def configuracoes_iniciais(self, partida, tamanho, dificuldade):
		self._tipo_partida = partida
		self._model.cria_tabuleiro(tamanho)
		self._model.set_dificuldade(dificuldade)

	def vez_humano(self, coord_nova_peca):
		self.mudar_adversario()
		self._view.trocar_jogador_atual(self._jogador_atual)
		self._erro = False
		
		self.inserir_peca(coord_nova_peca)
		
		if self.verifica_empate():
			self._erro = True
			self._view.mensagem_empate()

		return self._jogador_atual, self._erro

	def vez_ia(self):
		self.mudar_adversario()
		self._view.trocar_jogador_atual(self._jogador_atual)
		
		coord = self._model.encontrar_melhor_jogada()
		self.inserir_peca(coord)

		if self.verifica_empate():
			self._view.mensagem_empate()

		return coord[0],coord[1]

	def verifica_fim_jogo(self):
		if self._model.fim_de_jogo():
			self._view.mensagem_fim_de_jogo(self._jogador_atual) 

	def mudar_adversario(self):
		self._jogador_atual = Jogador(not self._jogador_atual.value)

	def inserir_peca(self, coord):
		try:
			self._model.inserir_peca(coord, self._jogador_atual)
		except Exception:
			self._view.msg_erro_inserir_peca()
			self.mudar_adversario()
			self._view.trocar_jogador_atual(self._jogador_atual)
			self._erro = True

	def verifica_empate(self):
		return self._model.empate()	 