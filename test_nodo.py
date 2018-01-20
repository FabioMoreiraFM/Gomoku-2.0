import unittest
import nodo
from jogador import *

class TestNodoMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.nodo = nodo.Nodo([2,3], Jogador.ADVERSARIO_1)

    def test_verifica_coordenada(self):
        self.assertEqual([2,3], self.nodo.get_coordenada())

    def test_verifica_dono(self):
        self.assertEqual(Jogador.ADVERSARIO_1, self.nodo.get_dono())

    def test_modifica_dono(self):
        self.nodo.set_dono(Jogador.ADVERSARIO_2)

        self.assertEqual(Jogador.ADVERSARIO_2, self.nodo.get_dono())

        self.nodo.set_dono(Jogador.ADVERSARIO_1)

if __name__ == '__main__':
    unittest.main()