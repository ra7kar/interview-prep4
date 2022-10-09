# given a array, find the pivot point where sum of left equals sum of right side
# LeetCode problem
# https://leetcode.com/problems/find-pivot-index/

# lets do a TDD implementation (Test driven development)

from lib2to3.pgen2.tokenize import untokenize
import unittest
from numpy.testing._private.parameterized import parameterized

def find_pivot(py_list):

    t_sum = sum(py_list)
    l_sum = 0

    # t_sum - l_sum - py_list[i] == l_sum

    for i in range(len(py_list)):
        if t_sum - py_list[i] == 2*l_sum:
            return i
        
        l_sum += py_list[i]
    
    return -1

class TestFindPivot(unittest.TestCase):
    @parameterized.expand([
        ([11,4,11], 1),
        ([2,4,5,6,5,4,2], 3),
        ([2,8,5,6,5,4,2], -1),
    ])
    def test_find_pivot(self, input, result):
        self.assertEqual(find_pivot(input), result)

if __name__ == "__main__":
    unittest.main()



