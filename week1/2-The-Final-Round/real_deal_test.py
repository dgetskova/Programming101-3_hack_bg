from real_deal import *
import unittest


class RealDealTest(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words((["apple", "banana", "apple", "pie", "no"])), {'apple': 2, 'pie': 1, 'banana': 1, 'no': 1})

    def test_unique_words_count(self):
        self.assertEqual(
            unique_words_count(["python", "python", "python", "ruby"]), 2)

    def test_nan_expand(self):
        self.assertEqual(nan_expand(5), 'Not a Not a Not a Not a Not a Nan')

    def test_is_prime(self):
        self.assertTrue(is_prime(23))

    def test_is_prime_no(self):
        self.assertFalse(is_prime(222))

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(1000), [(2, 3), (5, 3)])

    def test_group(self):
        self.assertEqual(group([1, 1, 1, 2, 3, 1, 1]),[[1, 1, 1], [2], [3], [1, 1]])

    def test_max_consecutive(self):
        self.assertEqual(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]), 3)

    def test_groupby(self):
        self.assertEqual(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]), {
            0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]})

    def test_count_of_consist(self):
        self.assertEqual(count_of_consist(27, 3), 3)

    def test_prepare_meal_simple3(self):
        self.assertEqual(prepare_meal(3), ' three')

    def test_prepare_meal_3and5(self):
        self.assertEqual(prepare_meal(45), ' three three and five')

    def test_prepare_meal_3and5_big_num(self):
        self.assertEqual(prepare_meal(225*3), ' three three three and five five')

    def test_prepare_meal_empty(self):
        self.assertEqual(prepare_meal(7), '')
if __name__ == '__main__':
    unittest.main()
