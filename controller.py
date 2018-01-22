import model
import view
from jogador import *

class Controller:
	_model = None
	_view = None
	_jogador_atual = Jogador.ADVERSARIO_2

	def __init__(self):
		self._model = model.Model()
		self._view = view.View()

		self.iniciar_jogo(self._view.opcao_jogo())

	def iniciar_jogo(self, opcao):
		self._model.cria_tabuleiro(self._view.tamanho_tabuleiro())
		self._view.exibir_tabuleiro(self._model.get_tabuleiro())
		
		if opcao:
			self.partida_HxH()
		else:
			self.partida_HxIA()

		self._view.mensagem_fim_de_jogo(self._jogador_atual)

	def partida_HxH(self):
		while self._model.fim_de_jogo():
			self.mudar_adversario()
			coord = self._view.escolha_posicao_inserir_peca()
			self.inserir_peca(coord)			

	def partida_HxIA(self):
		while self._model.fim_de_jogo():
			self.mudar_adversario()

			if self._jogador_atual == Jogador.ADVERSARIO_1:
				coord = self._view.escolha_posicao_inserir_peca()
			else:
				coord = self._model.encontrar_melhor_jogada()
			
			self.inserir_peca(coord)

	def mudar_adversario(self):
		self._jogador_atual = Jogador(not self._jogador_atual.value)

	def inserir_peca(self, coord):
		try:
			self._model.inserir_peca(coord, self._jogador_atual)
		except Exception:
			self._view.msg_erro_inserir_peca()
			self.mudar_adversario()
		else:
			self._view.exibir_tabuleiro(self._model.get_tabuleiro())
			self._view.exibir_encadeamento(self._model.get_encadeamento())	

x = Controller()