# Breadth first traversal
# lets use the queue to help achieve the traversal level wise.

# lets start with Test driven development

#std
import unittest
from collections import deque

#internal
from binary_tree import BinaryTree

#external
from numpy.testing._private.parameterized import parameterized

def breadth_first(bt):
    res = [ ]
    cur = bt.root
    q = deque([cur])

    while q:
        cur = q.popleft()
        res.append(cur.val)

        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
        
    return res


class TestBreadthFirst(unittest.TestCase):
    @parameterized.expand([
        ([4,2,3,1,6,5,7,8], [4,2,6,1,3,5,7,8]),
    ])
    
    def test_breadth_first(self, input, result):
        bt = BinaryTree(input)
        self.assertEqual(breadth_first(bt), result)

if __name__ == "__main__":
    unittest.main()

