import Tests.test_controle_encadeamento as tce
import Tests.test_nodo as tn
import Tests.test_tabuleiro as tt
import unittest

def suite():

    suite = unittest.TestSuite()

    suite.addTest (tce.TestControleEncadeamentoMethods())
    suite.addTest (tn.TestNodoMethods())
    suite.addTest (tt.TestTabuleiroMethods())

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)