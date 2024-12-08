import pytest



@pytest.fixture
def values():
    return [95, 82, 74, 63, 89]


def test_more_then_0(values):
    assert all(value >= 0 for value in values)

def test_sum_max_95(values):
    assert max(values) == 95

def test_average(values):
    average = sum(values) / len(values)
    assert average > 70
