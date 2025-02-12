import unittest
from suma import suma

class MyTestCase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma( a=1,b=2), 3)


if __name__ == '__main__':
    unittest.main()