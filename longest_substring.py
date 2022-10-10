# longest substring without repeating.
# LeetCode problem - https://leetcode.com/problems/longest-substring-without-repeating-characters/

# lets implement with the TDD approach, (Test driven approach)


from curses import longname
from re import I
import unittest
from numpy.testing._private.parameterized import parameterized

class TestLongestSubstring(unittest.TestCase):
    @parameterized.expand([
        ('abcabcbd', 3),
        ('abcabcbb', 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        ("nfpdmpi", 5),
        ("bbtablud", 6),
        ("wobgrovw", 6),
        ("bddsdddcvssvvcccbbbb", 4),
    ])

    def test_longest_substring(self, input, result):
        self.assertEqual(longest_substring(input), result)


def longest_substring(s):

    if s is None:
        return [ ]

    s_len = len(s)
    left = right = 0
    res = 0
    seen = { }

    while left < s_len and right < s_len:

        cur = s[right]
        if cur not in seen:
            seen[cur] = right
            res = max(res, right-left+1)
            right += 1
        else:
            left = max(left, seen[cur]+1)
            if s[left] == s[right]:
                left = right
            seen[cur] = right
            res = max(res, right-left+1)
            right += 1

    return res


if __name__ == "__main__":
    unittest.main()




