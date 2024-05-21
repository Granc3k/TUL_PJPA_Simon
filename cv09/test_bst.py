from bst import BST
import pytest


def test_add_items():
    tree = BST()
    tree.add(5)
    tree.add(10)
    tree.add(1)

    assert [5, 1, 10] == tree.bfs()


def test_different_types():
    tree = BST()
    with pytest.raises(TypeError) as e_info:
        tree.add(1)
        tree.add("str")
        tree.add(1.23)


def test_empty_tree_len():
    tree = BST()
    assert len(tree) == 0


def test_len():
    tree = BST()
    tree.add(1)
    tree.add(11)
    tree.add(1)
    assert len(tree) == 3


def test_iterator():
    tree = BST()
    tree.add(6)
    tree.add(6)
    tree.add(4)
    tree.add(17)
    tree.add(-1)
    tree.add(2)
    except_results = [6, 6, 17, 4, -1, 2]
    assert len(tree) == len(except_results)
    for index, item in enumerate(tree):
        print(item)
        assert item == except_results[index]


def test_find():
    tree = BST()
    tree.add(6)
    tree.add(1)
    tree.add(10)
    assert 10 in tree


def test_not_find():
    tree = BST()
    tree.add(6)
    tree.add(11)
    tree.add(25)
    assert 10 not in tree
