import Model.nodo as nodo
import Model.tabuleiro as tabuleiro
import Model.ia as ia
import Model.controleEncadeamento as controleEncadeamento

class Model:
	_tabuleiro = None
	_ia = None
	_controle_encadeamento = None
	_dificuldade = None

	def __init__(self):
		self._controle_encadeamento = controleEncadeamento.ControleEncadeamento() 
		self._ia = ia.IA(self._controle_encadeamento)

	def cria_tabuleiro(self, tamanho):
		self._tabuleiro = tabuleiro.Tabuleiro(tamanho)
		self.set_tabuleiro()

	def set_tabuleiro(self):
		self._ia.set_tabuleiro(self._tabuleiro)
		self._controle_encadeamento.set_tabuleiro(self._tabuleiro)

	def get_tabuleiro(self):
		return self._tabuleiro.get_tabuleiro()

	def fim_de_jogo(self):
		return self._controle_encadeamento.fim_de_jogo()

	def inserir_peca(self, coord, novo_dono):
		if self._tabuleiro.inserir_peca(coord, novo_dono):
			raise Exception
		self.atualiza_controle_encadeamento(coord)

	def atualiza_controle_encadeamento(self, coord):
		self._controle_encadeamento.atualiza(coord)

	def encontrar_melhor_jogada(self):
		self._ia.minimax(self._dificuldade)
		return self._ia.melhor_jogada()

	def get_encadeamento(self):
		return self._controle_encadeamento.get_encadeamento()

	def set_dificuldade(self, dificuldade):
		self._dificuldade = dificuldade

	def empate(self):
		return True if len(self._tabuleiro.get_nodos_disponiveis().keys()) == 0 else False
