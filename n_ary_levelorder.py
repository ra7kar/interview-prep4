# implement n-ary tree level order 
# LeetCode problem 
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# lets use the TDD - Test driven development approach.

import unittest
from numpy.testing._private.parameterized import parameterized
from binary_tree import BinaryTree
from collections import deque

def nary_level_order(bt):
    if bt.root is None:
        return [ ]
    
    cur = bt.root
    q = deque([cur])
    res = []

    while q:
        q_len = len(q)
        level = [ ]
        tmp_q = deque()

        for i in range(q_len):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                tmp_q.append(cur.left)
            if cur.right:
                tmp_q.append(cur.right)

        res += [level]
        q = tmp_q

    return res





class TestNAryLevelOrder(unittest.TestCase):
    @parameterized.expand([
        ([4,2,3,1,6,5,7,8], [[4],[2,6],[1,3,5,7],[8]]),
        ([4,2,1,9,6,8,7,5], [[4], [2, 9], [1, 6], [5, 8], [7]]),
    ])

    def test_nary_level_order(self, input, result):
        bt = BinaryTree(input)
        self.assertEqual(nary_level_order(bt), result)



if __name__ == "__main__":
    unittest.main()
    # l = [4,2,3,1,6,5,7,8] 
    # bt = BinaryTree(l)
    # print(nary_level_order(bt))
