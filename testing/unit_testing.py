import math
import unittest
def sqr_root(num):
    return math.sqrt(num)

class TestClass(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(sqr_root(100),10,'The result should be 10.')

if __name__ == '__main__':
    unittest.main()
