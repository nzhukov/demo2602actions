def add(a, b): 
    return a + b

def minus(a, b):
    return a - b


def test_add():
    assert add(2, 3) == 5


def test_minus():
    assert minus(2, 3) == -2
