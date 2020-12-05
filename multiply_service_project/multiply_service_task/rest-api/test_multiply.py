import unittest
from .multiply import get_multiply


class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(get_multiply([1, 2, 3, 4]), 24)
        self.assertEqual(get_multiply([5, 5, 5]), 125)
        self.assertEqual(get_multiply([-5, -5, 5]), -125)


if __name__ == '__main__':
    unittest.main()
