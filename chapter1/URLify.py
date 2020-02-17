import unittest


def URLify(s, true_len):
    """
    Replace all spaces in a string with '%20'. Assume the string has sufficient space at the end
    to hold the additional characters and you are given the true length of the string.
    :param s:
    :param true_len:
    :return:
    """
    assert true_len >= 0, "Invalid true length: ({0})".format(true_len)

    if true_len == 0:
        return ""

    # Count the number of spaces from index 0 to true_len
    space_cnt = 0
    for i in range(true_len):
        if s[i] == ' ':
            space_cnt += 1

    # Copy each char starting from the end of the string.
    # s_idx is the index of the char being copied.
    # res_odx is the index where it's being copied.
    s_idx = true_len - 1
    res_idx = s_idx + (space_cnt * 2)

    while s_idx >= 0:
        if s[s_idx] != ' ':
            s[res_idx] = s[s_idx]
            res_idx -= 1
        else:
            s[res_idx] = '0'
            s[res_idx - 1] = '2'
            s[res_idx - 2] = '%'
            res_idx -= 3

        s_idx -= 1

    return ''.join(s)


class TestURLify(unittest.TestCase):

    def test_URLify(self):
        self.assertEqual(URLify([], 0), '')
        self.assertEqual(URLify([' ', '', ''], 1), '%20')
        self.assertEqual(URLify(['a', ' ', '', ''], 2), 'a%20')
        self.assertEqual(URLify([' ', 'a', ' ', ''], 2), '%20a')
        self.assertEqual(URLify(['a', ' ', 'b', '', ''], 3), 'a%20b')
        self.assertEqual(URLify(['a', ' ', ' ', 'b', '', '', '', ''], 4), 'a%20%20b')


if __name__ == '__main__':
    unittest.main()
