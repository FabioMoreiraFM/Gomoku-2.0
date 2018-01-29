import model
import view
from jogador import *

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
		self._erro = False
		self.mudar_adversario()
		self.inserir_peca(coord_nova_peca)
		return self._jogador_atual, self._erro

	def vez_ia(self):
		self.mudar_adversario()
		coord = self._model.encontrar_melhor_jogada()
		self.inserir_peca(coord)
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
			self._erro = True

x = Controller()