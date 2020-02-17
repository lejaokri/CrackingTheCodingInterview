import unittest


def isOneAway(s1, s2):
    """
    There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check
    if they are one edit (or zero edit) away.
    """

    s1_len = len(s1)
    s2_len = len(s2)

    if abs(s1_len - s2_len) > 1:
        return False

    (shorter, longer, shorter_len, longer_len) = (s1, s2, s1_len, s2_len) \
        if s1_len < s2_len else (s2, s1, s2_len, s1_len)
    diff = False
    s_idx = 0
    l_idx = 0

    while s_idx < shorter_len:
        if shorter[s_idx] == longer[l_idx]:
            s_idx += 1
            l_idx += 1
            continue
        
        if diff:
            return False

        diff = True
        if s1_len == s2_len:
            s_idx += 1

        l_idx += 1

    return True


class TestUnit(unittest.TestCase):

    def test_1(self):
        self.assertTrue(isOneAway('', ''))
        self.assertTrue(isOneAway('a', 'b'))
        self.assertTrue(isOneAway('a', 'ba'))
        self.assertTrue(isOneAway('pale', 'ple'))
        self.assertTrue(isOneAway('pales', 'pale'))
        self.assertTrue(isOneAway('pale', 'bale'))
        self.assertFalse(isOneAway('pale', 'bae'))
        self.assertFalse(isOneAway('pale', 'pael'))


if __name__ == '__main__':
    unittest.main()
