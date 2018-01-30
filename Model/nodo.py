class Nodo:

	_coordenada = None
	_dono = None

	def __init__(self, coordenada, dono):
		self._coordenada = coordenada
		self._dono = dono

	def get_coordenada(self):
		return self._coordenada

	def get_dono(self):
		return self._dono

	def set_dono(self, novo_dono):
		self._dono = novo_dono