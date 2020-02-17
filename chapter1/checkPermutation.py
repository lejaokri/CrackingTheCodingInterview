import unittest


def checkPermutation(s1, s2):
    """
    Given two strings, write a method to decide if one is a permutation of the other.
    :param s1: str
    :param s2: str
    :return: bool
    """
    map_s = {}

    for c in s1:
        if c not in map_s:
            map_s[c] = 0
        map_s[c] += 1

    for c in s2:
        if c not in map_s or map_s[c] == 0:
            return False
        map_s[c] -= 1

    return sum(map_s.values()) == 0


class TestCheckPermutation(unittest.TestCase):

    def test_checkPermutation(self):
        self.assertTrue(checkPermutation('', ''))
        self.assertTrue(checkPermutation('a', 'a'))
        self.assertTrue(checkPermutation('ab', 'ba'))
        self.assertTrue(checkPermutation('abc', 'cab'))
        self.assertFalse(checkPermutation('abb', 'abc'))
        self.assertFalse(checkPermutation('aab', 'bba'))
        self.assertFalse(checkPermutation('aba', 'dba'))


if __name__ == '__main__':
    unittest.main()
