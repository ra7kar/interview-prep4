# give a string find the longest Palindromic string that can be created from the string s
# LeetCode problem
# https://leetcode.com/problems/longest-palindromic-substring/


# TDD - Test driven approach.

# 'racecar'
# 'abba'
# approach, - loop through the string, and for every string check left and right to see
# if they are the same, if same the update that to the res string and res_len
# we will have even and odd characters in the sting which need to be addressed

import unittest
from numpy.testing._private.parameterized import parameterized

class TestPalindrome(unittest.TestCase):
    @parameterized.expand([
        ('racecar' , 'racecar'),
        ('aba', 'aba'),
        ('abba', 'abba'),
        ('abbacsfs', 'abba'),
    ])
    
    def test_palindrome(self, string, result):
        rec = find_palindromic_string(string)
        self.assertEqual(rec, result)

def find_palindromic_string(s):

    # return values
    res = [ ]
    res_len = 0
    # we will used left and right pointers
    # loop through the string
    for i in range(len(s)):
        if len(s) % 2 != 0:
            # odd string length
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if res_len < len(s[left:right+1]):
                    res = s[left:right+1]
                    res_len = len(res)

                left -= 1
                right += 1
        else:
            # even string length
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right+1]) > res_len:
                    res = s[left:right+1]
                    res_len = len(res)
                
                left -= 1
                right += 1

        
    return res

unittest.main()

