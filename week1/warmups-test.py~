import unittest

from warmups import *


class WarmUps (unittest.TestCase):

    def test_fact(self):
        self.assertEqual(fact(5), 120)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)

    def test_fac_to_digits(self):
        self.assertEqual(fac_to_digits(999), 1088640)

    def test_sum_of_divisors_non_divisors(self):
        self.assertEqual(sum_of_divisors(7), 8)

    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(10), 10+5+2+1)

    def test_is_prime_yes(self):
        self.assertTrue(is_prime(13))

    def test_is_prime_no(self):
        self.assertFalse(is_prime(22))

    def test_palindrome_yes(self):
        self.assertTrue(palindrome(1996991))

    def test_palindrome_no(self):
        self.assertFalse(palindrome(1996))

    def test_count_digits(self):
        self.assertEqual(count_digits(123456), 6)

    def test_to_digits(self):
        self.assertEqual(to_digits(123), [1,2,3])

    def test_count_vowels(self):
        self.assertEqual(count_vowels("A nice day to code!"), 8)

    def test_char_histogram(self):
        self.assertEqual(char_histogram("AAAAaaa!!!D"), {
            'A': 4, 'a': 3, '!': 3, 'D': 1})

    def test_p_scope(self):
        self.assertEqual(p_score(198), 6)

    def test_is_increasing_yes(self):
        self.assertTrue(is_increasing([1, 5, 20]))

    def test_is_increasing_no(self):
        self.assertFalse(is_increasing([1, 5, 5, -20]))

    def test_next_hack(self):
        self.assertEqual(next_hack(8031), 8191)

if __name__ == '__main__':
    unittest.main()
