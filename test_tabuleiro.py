import unittest
import tabuleiro
from jogador import *

class TestTabuleiroMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.tabuleiro = tabuleiro.Tabuleiro(10)

    def test_inserir_peca(self):
        self.tabuleiro.inserir_peca([2,3], Jogador.ADVERSARIO_1)

        dono = self.tabuleiro.get_tabuleiro()[2][3].get_dono()
        self.assertEqual(Jogador.ADVERSARIO_1, dono)

        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[2][3])

    def test_remover_peca(self):
        self.tabuleiro.inserir_peca([0,0], Jogador.ADVERSARIO_2)
        novo_nodo = self.tabuleiro.get_tabuleiro()[0][0]
        self.tabuleiro.remover_peca(novo_nodo)

        self.assertEqual(Jogador.ESPACO_LIVRE, novo_nodo.get_dono())

    def test_verifica_quantidade_nodos_disponiveis(self):
        self.tabuleiro.inserir_peca([0,0], Jogador.ADVERSARIO_2)
        self.tabuleiro.inserir_peca([1,1], Jogador.ADVERSARIO_2)
        self.tabuleiro.inserir_peca([2,2], Jogador.ADVERSARIO_2)
        self.tabuleiro.inserir_peca([3,3], Jogador.ADVERSARIO_2)

        quantidade_nodos_disponiveis = len(self.tabuleiro.get_nodos_disponiveis().keys())
        self.assertEqual(96, quantidade_nodos_disponiveis)

        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[0][0])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[1][1])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[2][2])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[3][3])

    def test_inserir_peca_mesma_posicao(self):
        self.tabuleiro.inserir_peca([0,0], Jogador.ADVERSARIO_2)

        self.assertEqual(1, self.tabuleiro.inserir_peca([0,0], Jogador.ADVERSARIO_1))

        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[0][0])


if __name__ == '__main__':
    unittest.main()