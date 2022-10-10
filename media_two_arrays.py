# median of two array
# LeetCode problem
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# TDD - Test driven development

import unittest
from numpy.testing._private.parameterized import parameterized

class TestMedianTwoArrays(unittest.TestCase):
    @parameterized.expand([
        ([10,20,40,50], [30], 30),
        ([10,20,40,50], [50], 40),

    ])

    def test_median_of_two_arrays(self, input_a, input_b, result):
        self.assertEqual(median_array(input_a, input_b), result)

def median_array(a, b):

    arr = sorted(a + b)

    n = len(arr)

    if n % 2 == 0:      # even number count in array
        res = (arr[int(n/2)] + arr[int(n/2)-1])/2
    else:
        res = arr[int(n/2)]

    return res


if __name__ == "__main__":
    unittest.main()
