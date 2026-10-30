
print("Задача А")
print("Условие: определить, является ли бинарное дерево зеркальным отражением самого себя")
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_mirror(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    return (left.val == right.val and
            is_mirror(left.left, right.right) and
            is_mirror(left.right, right.left))


def is_symmetric(root):
    if root is None:
        return True
    return is_mirror(root.left, root.right)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric(root))


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(is_symmetric(root2))


print("Задача В")
print("Условие: найти длину самого длинного пути между любыми двумя узлами дерева. Длина измеряется количеством рёбер")


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter

        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    height(root)
    return diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter_of_tree(root))


root2 = TreeNode(1)
root2.left = TreeNode(2)

print(diameter_of_tree(root2))

print("Задача С")
print("Условие: проверить, находятся ли два узла на одной глубине, но имеют разных родителей")
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_node(root, value, depth=0, parent=None):
    if root is None:
        return None

    if root.val == value:
        return (depth, parent)

    left = find_node(root.left, value, depth + 1, root)

    if left is not None:
        return left

    return find_node(root.right, value, depth + 1, root)


def is_cousins(root, x, y):
    first = find_node(root, x)
    second = find_node(root, y)

    if first is None or second is None:
        return False

    return first[0] == second[0] and first[1] != second[1]



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(is_cousins(root, 4, 3))


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(5)

print(is_cousins(root2, 5, 4))