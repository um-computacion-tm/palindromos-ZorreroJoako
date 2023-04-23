import unittest 
from Palindromo_Recursividad import es_palindromo_recursivo

class TestPalindromo(unittest.TestCase):
    def test_palindromo1(self):
        self.assertTrue(es_palindromo_recursivo("anita lava la tina"))

    def test_palindromo2(self):
        self.assertTrue(es_palindromo_recursivo("neuquen"))

    def test_palindromo3(self):
        self.assertFalse(es_palindromo_recursivo("Hola mundo"))

if __name__ == '__main__':
    unittest.main()
