import unittest
from funcionesMatematicas import sumar, restar, multiplicar, dividir

#clase que recoge las pruebas unitarias
class testFunciones(unittest.TestCase):

    def test_sumar(self):    # Pruebas para la función de suma
        self.assertEqual(sumar(4, 3), 7)
        self.assertEqual(sumar(-2, 1), -1)    
        self.assertEqual(sumar(-1, -5), -6) 

    def test_restar(self):   # Pruebas para la función de resta
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(-1, 1), -2)    
        self.assertEqual(restar(-1, -3), 2) 

    def test_multiplicar(self):  # Pruebas para la función de multiplicación
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(-2, 2), -4)    
        self.assertEqual(multiplicar(-2, -4), 8) 

    def test_dividir(self):  # Pruebas para la función de división
        self.assertEqual(dividir(8, 2), 4)
        self.assertEqual(dividir(12, 3), 4)    
        with self.assertRaises(ValueError): # Comprobación de la excepción generada al dividir por cero
            dividir(10, 0)


if __name__ == '__main__':
    unittest.main()     
     