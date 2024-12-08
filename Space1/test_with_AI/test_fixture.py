import pytest

@pytest.fixture
def value():
    return [1,2,3,4,5]

def test_slog(value):
    assert sum(value) == 15

def test_1_el(value):
    assert value[3] == 4

