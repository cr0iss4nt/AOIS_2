import unittest

from number_functions import index_form, number_perfect_conjunctive_normal_form, number_perfect_disjunctive_normal_form


class TestNumberFunctions(unittest.TestCase):
    def test_index_form(self):
        formula = "(A&B)|!C"
        self.assertEqual(index_form(formula), 171)

    def test_number_perfect_conjunctive_normal_form(self):
        formula = "(A&B)|!C"
        self.assertEqual(number_perfect_conjunctive_normal_form(formula), [1, 3, 5])

    def test_number_perfect_disjunctive_normal_form(self):
        formula = "(A&B)|!C"
        self.assertEqual(number_perfect_disjunctive_normal_form(formula), [0, 2, 4, 6, 7])
