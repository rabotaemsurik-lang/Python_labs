from task3 import AppleTree, Gardener, Apple

def test_apple_growing():
    a = Apple(0)
    a.grow()
    assert a._state == "Цвітіння"

def test_tree_grow():
    t = AppleTree(3)
    t.grow_all()
    assert t.apples[0]._state == "Цвітіння"

def test_all_are_ripe():
    t = AppleTree(1)
    t.grow_all()
    t.grow_all()
    t.grow_all()
    assert t.all_are_ripe() is True
