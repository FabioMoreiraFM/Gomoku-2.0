import nodo
import tabuleiro
import ia
import controleEncadeamento

class Model:
	_tabuleiro = None
	_ia = None
	_controle_encadeamento = None

	def __init__(self):
		self._controle_encadeamento = controleEncadeamento.ControleEncadeamento() 
		self._ia = ia.IA(self._controle_encadeamento)

	def cria_tabuleiro(self, tamanho):
		self._tabuleiro = tabuleiro.Tabuleiro(tamanho)
		self.set_tabuleiro_ia()

	def set_tabuleiro_ia(self):
		self._ia.set_tabuleiro(self._tabuleiro)

	def get_tabuleiro(self):
		return self._tabuleiro.get_tabuleiro()

	def fim_de_jogo(self):
		return self._ia.fim_de_jogo(self._controle_encadeamento.get_encadeamento())

	def inserir_peca(self, coord, novo_dono):
		try:
			self._tabuleiro.inserir_peca(coord, novo_dono)
		except Exception, e:
			print e
		self.atualiza_controle_encadeamento(coord)

	def atualiza_controle_encadeamento(self, coord):
		self._controle_encadeamento.atualiza(self._tabuleiro.get_tabuleiro(), coord)

	def encontrar_melhor_jogada(self):
		self._ia.minimax(3)
		return self._ia.melhor_jogada()

	def get_encadeamento(self):
		return self._controle_encadeamento.get_encadeamento()