import pytest


@pytest.fixture
def values():
    return [10, 20, 30, 40, 50]


def test_2(values):
    assert all(value % 2 == 0 for value in values)

def test_sum(values):
    test_id = sum(values)
    assert test_id > 100


def test_middle_val(values):
    middle_val = sum(values) / len(values)
    assert middle_val > 20
