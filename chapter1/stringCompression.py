import unittest

def stringCompress(s):
    """
    Implement a method to perform basic string compression using the counts
    of repeated characters. eg: "aabcccccaaa" -> "a2b1c5a3".
    If the compressed string would not become shorter than the original string,
    then return the original string.
    """
    if not s:
        return s

    s_len = len(s)
    compressed_len = _countCompressedLength(s)
    if compressed_len >= s_len:
        return s

    # At this point, we know the compressed str will be shorter. So build it.
    prev = s[0]
    curr_char_count = 0
    res = [] 

    for c in s:
        if c == prev:
            curr_char_count += 1
            continue
        
        res.append(prev + str(curr_char_count))
        curr_char_count = 1 
        prev = c

    # Dont forget to include the rest
    res.append(prev + str(curr_char_count))

    return ''.join(res)

def _countCompressedLength(s):
    curr_char_count = 0
    res = 0

    prev = s[0]
    for c in s:
        if c == prev:
            curr_char_count += 1
            continue

        res += 1 + len(str(curr_char_count))
        curr_char_count = 1
        prev = c

    # add the remaining
    res += 1 + len(str(curr_char_count))
    return res


class TestUnit(unittest.TestCase):

    def test_1(self):
        self.assertEqual(stringCompress(''), '')
        self.assertEqual(stringCompress('a'), 'a')
        self.assertEqual(stringCompress('aa'), 'aa')
        self.assertEqual(stringCompress('aaa'), 'a3')
        self.assertEqual(stringCompress('aaab'), 'aaab')
        self.assertEqual(stringCompress('aaabb'), 'a3b2')
        self.assertEqual(stringCompress('aabcccccaaa'), 'a2b1c5a3')


if __name__ == '__main__':
    unittest.main()

