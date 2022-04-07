from logging import root


class TreeNode:
    def __init__(self, key, val=None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def recursive_add(self, new_node, curr_node, value):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = new_node
            else:
                self.recursive_add(curr_node.left, value)
        else:
            if curr_node.right == None:
                curr_node.right = new_node
            else:
                self.recursive_add(curr_node.right, value)

    def add(self, key, value):
        new_node = TreeNode(key, value)
        if self.root is None:
            self.root = new_node
            return
        # self.recursive_add(self.root, new_node)

    # Time Complexity: O(log n)
    # Space Complexity: O(1)

    def recursive_find(self, curr_node, new_node, key):
        # curr_node = TreeNode(key, self.value)
        if self.key < curr_node.key:
            if curr_node.left == None:
                curr_node.left = new_node
            else:
                self.recursive_find(curr_node.left, key)
        else:
            if curr_node.right == None:
                curr_node.right = new_node
            else:
                self.recursive_find(curr_node.right, key)

    def find(self, key):
        if self.root == None:
            return None

        return self.recursive_find(self.root, key)

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def recursive_inorder(self, node, tree_list):
        if node is not None:
            self.recursive_inorder(node.left, tree_list)
            tree_list.append({
                "key": node.key,
                "value": node.value
            })
            self.recursive_inorder(node.right, tree_list)

    def inorder(self):
        tree_list = []
        self.recursive_inorder(self.root, tree_list)

        return tree_list

    # Time Complexity:
    # Space Complexity:
    def recursive_preorder(self, tree_node, tree_list):
        if tree_node is not None:
            tree_list.append({
                "key": tree_node.key,
                "value": tree_node.value
            })
            self.recursive_preorder(tree_node.left, tree_list)
            self.recursive_preorder(tree_node.right, tree_list)

    def preorder(self):
        tree_list = []
        self.recursive_preorder(self.root, tree_list)
        return tree_list

    # Time Complexity:
    # Space Complexity:

    def recursive_postorder(self, tree_node, tree_list):
        if tree_node is not None:
            self.recursive_postorder(tree_node.left, tree_list)
            self.recursive_postorder(tree_node.right, tree_list)
            tree_list.append({
                "key": tree_node.key,
                "value": tree_node.value
            })

    def postorder(self):
        tree_list = []
        self.recursive_postorder(self.root, tree_list)
        return tree_list

    # Time Complexity:
    # Space Complexity:

    def recursive_height(self, tree_node):
        if tree_node == None:
            return 0
        else:
            return max(
                self.recursive_height(tree_node.left),
                self.recursive_height(tree_node.right)
                + 1
            )

    def height(self):
        return self.recursive_height(self.root)


#   # Optional Method
#   # Time Complexity:
#   # Space Complexity:


    def bfs(self):
        pass


#   # Useful for printing


    def to_s(self):
        return f"{self.inorder()}"
