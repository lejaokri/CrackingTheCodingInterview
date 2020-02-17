import unittest


def isPalindromePermutation(s):
    """
    Given a string, write a function to check if it is a permutation of a palindrome.
    eg: "Tact Coa" -> True because it is a permutation of "taco cat"

    Assumption: s contains alphabet letters only, including space: ie [a-z,A-Z,' ']
    :param s:
    :return:
    """

    bitmap = 0
    for c in s:
        if c == ' ':
            continue

        idx = ord(c.lower()) - ord('a')

        # Flip the bit at idx. ie: if 1 set to 0, if 0 set to 1
        bit = (1 << idx)
        if bitmap & bit:
            bitmap &= ~bit
        else:
            bitmap |= bit

    # Return True if bitmap is 0 (all char in s appeared in even count)
    # or bitmap has only 1 bit set (1 char in s appeared in odd count)
    return bitmap == 0 or (bitmap & (bitmap - 1)) == 0


class TestUnit(unittest.TestCase):

    def test_1(self):
        self.assertTrue(isPalindromePermutation(''))
        self.assertTrue(isPalindromePermutation('a'))
        self.assertTrue(isPalindromePermutation('aba'))
        self.assertTrue(isPalindromePermutation('abb'))
        self.assertTrue(isPalindromePermutation('Tact Coa'))
        self.assertFalse(isPalindromePermutation('abc'))
        self.assertFalse(isPalindromePermutation('aab bac'))
        self.assertFalse(isPalindromePermutation('abad'))


if __name__ == '__main__':
    unittest.main()
