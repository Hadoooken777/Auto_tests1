import pytest



@pytest.fixture
def fruits():
    return ["banana", "cherry", "apple"]

def test_elem(fruits):
    assert all(len(fruit) > 3 for fruit in fruits)

def test_check_banana(fruits):
    assert "banana" in fruits

def test_first_elm(fruits):
    assert fruits[0] ==sorted(fruits)[0]















