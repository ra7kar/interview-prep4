# implement in-order traversal 
# implement iterative and recursive ways and test with unittest 

# TDD - Test Driven Development

# Std
import unittest
from collections import deque
from itertools import product

# Ext
from numpy.testing._private.parameterized import parameterized

# Internal
from binary_tree import BinaryTree

def inord_iter(bt):
    res = [ ]
    stack = deque()
    cur = bt.root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

    return res

def inord_recu(bt):
    res = [ ]
    def dfs(node):
        # visit left, root, right side
        #base case
        if node is None:
            return
        #left side node
        if node.left is not None:
            dfs(node.left)
        # root node
        res.append(node.val)

        # right side node
        dfs(node.right)

    dfs(bt.root)
    return res

def get_tests():
    tests = [
        ([4,2,1,3,6,5,7], [1,2,3,4,5,6,7]),
        ([4,2,1,3,6,5,7], [1,2,3,4,5,6,7]),
        ([4,2,1,3,6,5,7], [1,2,3,4,5,6,7]),
        ([4,2,1,3,6,5,7], [1,2,3,4,5,6,7]),
    ]
    return product([inord_iter, inord_recu] , tests)

class TestInOrderTraversal(unittest.TestCase):
    @parameterized.expand(get_tests())
    def test_inord_travers(self, func, test):
        bt = BinaryTree(test[0])
        self.assertEquals(func(bt), test[1])

if __name__ == "__main__":
    unittest.main()

