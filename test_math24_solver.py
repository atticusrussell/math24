import unittest
from solve_math24 import solve_math24
from fractions import Fraction

class TestMath24Solver(unittest.TestCase):
    def test_basic_solution(self):
        self.assertEqual(solve_math24([3, 3, 8, 8]), '8 / (3 - (8 / 3))')

    def test_no_solution(self):
        self.assertEqual(solve_math24([1, 1, 1, 1]), 'No solution possible')

    def test_decimal_input(self):
        self.assertEqual(solve_math24([1.5, 6, 8, 9]), '8 * (3/2 + (9 / 6))')

    def test_fraction_input(self):
        self.assertEqual(solve_math24([3/2, 6, 8, 9]), '8 * (3/2 + (9 / 6))')

if __name__ == '__main__':
    unittest.main()
