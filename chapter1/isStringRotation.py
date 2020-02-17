import unittest


def isStringRotation(s1, s2):
    """
    Given two strings, s1 and s2, return True is s2 is a rotation of s1
    using only one call to substr() function.
    eg: "waterbottle" is a rotation of "erbottlewat"
    """

    s1s1 = s1 + s1
    return s2 in s1s1

class TestUnit(unittest.TestCase):

    def test_1(self):
        self.assertTrue(isStringRotation("waterbottle", "erbottlewat"))
        

if __name__ == '__main__':
    unittest.main()

