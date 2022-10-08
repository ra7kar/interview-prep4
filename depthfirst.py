# - Test driven development approach (TDD)

# - standard
import unittest
from collections import deque
from itertools import product

# - External
from numpy.testing._private.parameterized import parameterized

# - Internal 
from binary_tree import BinaryTree

# implement depth first search iterative approach
def in_ord_iterative(bt):
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

# implement depth first search - recursive approach
def in_ord_recu(bt):
    res = [ ]
    def dfs(node):
        #base case
        if node is None:
            return

        # recursive section
        if node.left is not None:       # traverse left side node
            dfs(node.left)
        res.append(node.val)            # add root to the ret list
        if node.right is not None:      # traverse right side of the node
            dfs(node.right)
    
    dfs(bt.root)    
    return res

def get_tests():
    tests = [
        ([4,3,2,1,6,5,7], [1,2,3,4,5,6,7]),
        ([4,5,7,2,3,6], [2,3,4,5,6,7]),
    ]

    return product([in_ord_iterative, in_ord_recu], tests)

class TestDepthFirst(unittest.TestCase):
    @parameterized.expand(get_tests())

    def test_depth_first(self, func, test):
        bt = BinaryTree(test[0])
        self.assertEqual(func(bt), test[1])
        self.assertEqual(func(bt), test[1])



if __name__ == "__main__":
    unittest.main()

