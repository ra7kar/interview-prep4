# implement n-ary breadth first traversal.
# leetcode problem 
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# TDD - Test driven development

import unittest
from numpy.testing._private.parameterized import parameterized
from collections import deque

from binary_tree import BinaryTree

def nary_breadth_traversal(bt):
    if bt.root is None:
        return [ ]
    q = deque([bt.root])
    res = [ ]

    while q:
        q_len = len(q)
        level = [ ]
        tmp_q = deque()

        for _ in range(q_len):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                tmp_q.append(cur.left)
            if cur.right:
                tmp_q.append(cur.right)
        
        q = tmp_q
        res.append(level)

    return res


class TestNaryBreadthTraversal(unittest.TestCase):
    @parameterized.expand([
        ([4,2,3,1,6,5,7,8], [[4], [2, 6], [1, 3, 5, 7], [8]]),
    ])

    def test_nary_breadth_traversal(self, input, result):
        bt = BinaryTree(input)
        self.assertEqual(nary_breadth_traversal(bt), result)


if __name__ == "__main__":
    unittest.main()

    l = [4,2,3,1,6,5,7,8]
    bt = BinaryTree(l)
    print(nary_breadth_traversal(bt))