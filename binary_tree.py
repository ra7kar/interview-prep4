# implement a binary tree
# thanks to JV for the display tree code 
# https://stackoverflow.com/revisions/54074933/1

# Node class for the binary tree
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self):
        # No child.
        if self.right is None and self.left is None:
            if self.height:
                line = "({}, {})".format(self.val, self.height)
            else:
                line = "({})".format(self.val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            if self.height > 0:
                s = "({}, {})".format(self.val, self.height)
            else:
                s = "({})".format(self.val)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "-" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            if self.height:
                s = "({}, {})".format(self.val, self.height)
            else:
                s = "({})".format(self.val)
            u = len(s)
            first_line = s + x * "-" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        if self.height:
            s = "({}, {})".format(self.val, self.height)
        else:
            s = "({})".format(self.val)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "-" + s + y * "-" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# Binary tree class
class BinaryTree:
    def __init__(self, py_list=None) -> None:
        # Edge case
        if py_list is None:
            return [ ]

        #create a root attribute
        self.root = None

        # loop through the py_list
        for i in py_list:
            self.add(i)

    def add(self, val):
        
        if self.root is None:
            self.root = Node(val)
        else:
            self._add_helper(self.root, val)

    def _add_helper(self,node, val):
        
        # create a new node
        new_node = Node(val)

        # build the left side
        if val < node.val:
            if node.left is not None:
                self._add_helper(node.left, val)
            else:
                node.left = new_node
        else:
            if node.right is not None:
                self._add_helper(node.right, val)
            else:
                node.right = new_node

    def __iter__(self):
        def dfs(cur):
            # go to the left side
            if cur.left is not None:
                yield from dfs(cur.left)
            # get the root node
            yield cur

            # go to the right side
            if cur.right is not None:
                yield from dfs(cur.right)

        yield from dfs(self.root)
            
        
    def __str__(self):
        return ", ".join(str(i.val) for i in self)
            

if __name__ == "__main__":

    bt = BinaryTree([4,2,1,3,6,5,7])
    print(bt)
    print(bt.root)
