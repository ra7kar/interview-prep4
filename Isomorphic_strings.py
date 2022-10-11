# Isomorphic_strings 
# LeetCode problem : https://leetcode.com/problems/isomorphic-strings/

# do a TDD - Test driven development

import unittest
from numpy.testing._private.parameterized import parameterized

class TestIsomorphicStrings(unittest.TestCase):
    @parameterized.expand([
        ('abc', 'def', True),
        ('foo', 'bar', False),
        ('badc', 'baba', False),

    ])

    def test_isom_strings(self, s, t, result):
        self.assertEqual(isom_strings(s, t), result)


def isom_strings(s, t):

    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False

    map_s = { }
    map_t = { }

    for c1, c2 in zip(s, t):

        if c1 not in map_s and c2 not in map_t:
            map_s[c1] = c2
            map_t[c2] = c1

        elif map_s.get(c1) != c2 or map_t.get(c2) != c1:
            return False

    return True




if __name__ == "__main__":
    unittest.main()


    