import unittest
import tabuleiro
import controleEncadeamento
from jogador import *

class TestControleEncadeamentoMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.tabuleiro = tabuleiro.Tabuleiro(10)
        self.controle = controleEncadeamento.ControleEncadeamento()
        self.encadeamento = self.controle.get_encadeamento()
        self.controle.set_tabuleiro(self.tabuleiro)

    def test_encadeamento_tamanho_1(self):
        self.tabuleiro.inserir_peca([2,3], Jogador.ADVERSARIO_1)
        self.controle.atualiza([2,3])

        self.assertEqual(self.encadeamento[Jogador.ADVERSARIO_1][0], 1)

    def test_encadeamento_tamanho_5(self):
        self.tabuleiro.inserir_peca([0,0], Jogador.ADVERSARIO_1)
        self.controle.atualiza([0,0])
        
        self.tabuleiro.inserir_peca([0,1], Jogador.ADVERSARIO_1)
        self.controle.atualiza([0,1])
        
        self.tabuleiro.inserir_peca([0,2], Jogador.ADVERSARIO_1)
        self.controle.atualiza([0,2])
        
        self.tabuleiro.inserir_peca([0,3], Jogador.ADVERSARIO_1)
        self.controle.atualiza([0,3])
        
        self.tabuleiro.inserir_peca([0,4], Jogador.ADVERSARIO_1)
        self.controle.atualiza([0,4])

        self.assertEqual(self.encadeamento[Jogador.ADVERSARIO_1][4], 1)

        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[0][0])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[0][1])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[0][2])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[0][3])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[0][4])
        self.controle.get_encadeamento()[Jogador.ADVERSARIO_1][4] = 0

    def test_encadeamento_tamanho_maior_5(self):
        self.tabuleiro.inserir_peca([3,0], Jogador.ADVERSARIO_1)
        self.controle.atualiza([3,0])
        
        self.tabuleiro.inserir_peca([3,1], Jogador.ADVERSARIO_1)
        self.controle.atualiza([3,1])
        
        self.tabuleiro.inserir_peca([3,2], Jogador.ADVERSARIO_1)
        self.controle.atualiza([3,2])
        
        self.tabuleiro.inserir_peca([3,3], Jogador.ADVERSARIO_1)
        self.controle.atualiza([3,3])
        
        self.tabuleiro.inserir_peca([3,4], Jogador.ADVERSARIO_1)
        self.controle.atualiza([3,4])

        self.tabuleiro.inserir_peca([3,5], Jogador.ADVERSARIO_1)
        self.controle.atualiza([3,5])

        self.assertEqual(self.encadeamento[Jogador.ADVERSARIO_1][4], 1)

        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[3][0])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[3][1])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[3][2])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[3][3])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[3][4])
        self.tabuleiro.remover_peca(self.tabuleiro.get_tabuleiro()[3][5])
        self.encadeamento[Jogador.ADVERSARIO_1][4] = 0

if __name__ == '__main__':
    unittest.main()