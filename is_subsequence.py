# give a string check if its a subsequence of another string
# LeetCode problem
# https://leetcode.com/problems/is-subsequence/

# lets implement with the TDD approach, Test driven development

import unittest
from numpy.testing._private.parameterized import parameterized

class TestIsSubsequence(unittest.TestCase):

    @parameterized.expand([ 
        ('abc', 'dxzaddtdbc', True),
        ('jfk', 'asdrjfllasdfkadsaf', True),
        ('jfk', 'jasdf', False),
    ])
    def test_is_subsequence(self, s, t, result):
        self.assertEqual(is_subsequence(s, t), result)

def is_subsequence(s, t):
    s_len = len(s)
    t_len = len(t)

    if s_len > t_len:
        return False
    if s_len == 0:
        return True

    pointer = 0

    for c in t:
        if c == s[pointer]:
            pointer += 1
            if pointer >= s_len:
                break
    
    return pointer == s_len

if __name__ == "__main__":
    unittest.main()
