import unittest
from suma import suma, resta

class MyTestCase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma( a=1,b=2), 3)
    def test_resta(self):
        self.assertEqual(resta( a=2,b=1), 1)


if __name__ == '__main__':
    unittest.main()