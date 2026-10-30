class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Правый поворот
    def rotate_right(self, node):
        new_root = node.left
        middle = new_root.right

        new_root.right = node
        node.left = middle


        self.update_height(node)
        self.update_height(new_root)

        return new_root

    # поворот
    def rotate_left(self, node):
        new_root = node.right
        middle = new_root.left

        new_root.left = node
        node.right = middle

        self.update_height(node)
        self.update_height(new_root)

        return new_root

    # Восстановление баланса поддерева
    def balance(self, node):
        self.update_height(node)
        factor = self.balance_factor(node)


        if factor > 1:
            # Случай LR: сначала левый поворот у левого потомка
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)


            return self.rotate_right(node)


        if factor < -1:

            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)

            return self.rotate_left(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        return self.balance(node)

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left


            replacement = self.find_min(node.right)
            node.key = replacement.key

            node.right = self._delete(
                node.right, replacement.key
            )

        return self.balance(node)

    def search(self, key):
        node = self.root

        while node is not None:
            if key == node.key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return False

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def print_tree(self):
        if self.root is None:
            print("\nДерево пустое.")
            return

        print("\nДерево (правые потомки сверху, левые снизу):")
        self._print_tree(self.root, 0)
        print()

    def _print_tree(self, node, level):
        if node is None:
            return

        self._print_tree(node.right, level + 1)

        indent = "    " * level
        factor = self.balance_factor(node)
        print(
            f"{indent}{node.key} "
            f"(h={node.height}, b={factor})"
        )

        self._print_tree(node.left, level + 1)


def read_number():
    while True:
        try:
            return int(input("Введите целое число: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число.")


def main():
    tree = AVLTree()

    while True:
        print("\n1 — Добавить элемент")
        print("2 — Удалить элемент")
        print("3 — Найти элемент")
        print("4 — Показать дерево")
        print("5 — Вывести элементы по возрастанию")
        print("0 — Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            try:
                text = input("Введите числа через: ")
                numbers = list(map(int, text.split()))

                for key in numbers:
                    if tree.search(key):
                        print(f"Число {key} уже есть в дереве.")
                    else:
                        tree.insert(key)
                        print(f"Добавлен элемент {key}.")
                        tree.print_tree()

            except ValueError:
                print("Ошибка: вводите целые числа через пробел.")
        elif choice == "2":
            key = read_number()

            if tree.search(key):
                tree.delete(key)
                print(f"Удалён элемент {key}.")
            else:
                print("Такого значения нет в дереве.")

            tree.print_tree()

        elif choice == "3":
            key = read_number()

            if tree.search(key):
                print("Элемент найден.")
            else:
                print("Элемент не найден.")

        elif choice == "4":
            tree.print_tree()

        elif choice == "5":
            print("Элементы по возрастанию:", tree.inorder())

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Нет такого пункта меню.")


if __name__ == "__main__":
    main()