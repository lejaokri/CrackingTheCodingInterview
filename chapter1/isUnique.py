import unittest


def isUnique1(s):
    """
        Implement an algorithm to determine if a string has all unique character.
        What if you cannot use additional data structures.
        Assumption: s contains ASCII characters only.
    """

    c_map = [0] * 256
    for c in s:
        idx = ord(c)
        assert 0 <= idx <= 255, "Invalid character '{0}' detected.".format(c)

        if c_map[ord(c)]:
            return False
        c_map[ord(c)] = 1

    return True


def isUnique2(s):
    """
        Same as isUnique1() but supports only lower case ascii letters.
        Use a bitmap instead to improve storage complexity.
    """

    bitmap = 0
    for c in s:
        idx = ord(c) - ord('a')
        assert 0 <= idx <= 31, "Invalid character '{0}' detected.".format(c)

        if bitmap & (1 << idx):
            return False
        bitmap |= (1 << idx)

    return True


class TestIsUnique(unittest.TestCase):

    def test_isUnique1(self):
        self.assertTrue(isUnique1(''))
        self.assertTrue(isUnique1('a'))
        self.assertTrue(isUnique1('ab'))
        self.assertTrue(isUnique1('abc'))
        self.assertFalse(isUnique1('abb'))
        self.assertFalse(isUnique1('aab'))
        self.assertFalse(isUnique1('aba'))

    def test_isUnique2(self):
        self.assertTrue(isUnique2(''))
        self.assertTrue(isUnique2('a'))
        self.assertTrue(isUnique2('ab'))
        self.assertTrue(isUnique2('abc'))
        self.assertFalse(isUnique2('abb'))
        self.assertFalse(isUnique2('aab'))
        self.assertFalse(isUnique2('aba'))


if __name__ == '__main__':
    unittest.main()
