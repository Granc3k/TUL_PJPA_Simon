"""
Cvičení 9. - BVS

V tomto úkolu si zopakujete jednu z datových struktur, 
kterou je Binární vyhledávací strom (dále jen BVS).

Kompletní zadání je jako vždy na https://elearning.tul.cz/
"""


class Node:
    """
    Třída pro reprezentaci uzlu ve stromu
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """
    Třída pro reprezentaci binárního vyhledávacího stromu (BVS)
    """

    def __init__(self):
        self.root = None
        self.type = None

    def add(self, item):
        """
        Metoda pro přidání prvku do stromu
        """
        if self.root is None:
            self.root = Node(item)
            self.type = type(item)
        else:
            if not isinstance(item, self.type):
                raise TypeError("Zadaná hodnota není typu, co se hodí do stromu")
            self._add(self.root, item)

    def _add(self, node, item):
        if item <= node.value:
            if node.left is None:
                node.left = Node(item)
            else:
                self._add(node.left, item)
        else:
            if node.right is None:
                node.right = Node(item)
            else:
                self._add(node.right, item)

    def contains(self, item):
        """
        Metoda pro kontrolu, zda se prvek nachází ve stromu
        """
        return self._contains(self.root, item)

    def _contains(self, node, item):
        if node is None:
            return False
        if node.value == item:
            return True
        if item < node.value:
            return self._contains(node.left, item)
        return self._contains(node.right, item)

    def __len__(self):
        """
        Metoda pro získání počtu prvků ve stromu
        """
        return self._len(self.root)

    def _len(self, node):
        if node is None:
            return 0
        return 1 + self._len(node.left) + self._len(node.right)

    def __str__(self):
        """
        Metoda pro textovou reprezentaci stromu
        """
        return ", ".join(str(x) for x in self.bfs())

    def bfs(self):
        """
        Metoda pro procházení stromu do šířky
        """
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            if node is not None:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
        return result

    def __iter__(self):
        """
        Metoda pro iterativní procházení stromu
        """
        self.nodes = self.bfs()
        return self

    def __next__(self):
        """
        Metoda pro získání dalšího prvku při iterativním procházení stromu
        """
        if not self.nodes:
            raise StopIteration
        return self.nodes.pop(0)


def main():
    """
    Hlavní funkce pro testování funkčnosti BVS
    """
    tree = BST()
    """
    tree.add(5)
    tree.add(3)
    tree.add(7)
    print(tree)
    print(len(tree))
    print(5 in tree)
    print(10 in tree)
    for node in tree:
        print(node)
    """


if __name__ == "__main__":
    main()
