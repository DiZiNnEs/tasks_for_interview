import unittest

import script


class TestScript(unittest.TestCase):
    def test_count_multipliers(self):
        self.assertEqual(script.count_multipliers(2, 2), 4)
        self.assertEqual(script.count_multipliers(15, 23, 432), 149040)
        self.assertEqual(script.count_multipliers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 3628800)
        self.assertEqual(script.count_multipliers(2, 0), 0)


if __name__ == '__main__':
    unittest.main()
