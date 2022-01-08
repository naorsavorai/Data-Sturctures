import unittest

class TestStringMethods(unittest.TestCase):

    def test(self):
        self.assertEqual(1, 0)

    def test1(self):
        self.assertEqual(1, 23)

    def test2(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()