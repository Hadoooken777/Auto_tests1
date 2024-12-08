import pytest
from pygments.lexer import include


@pytest.fixture
def bio():
    return {"name": "John",
           "age": 30,
           "email": "john.doe@example.com"
            }

def test_check_name(bio):
    assert "name" in bio


def test_age(bio):
    assert bio["age"] >= 18


def test_mail(bio):
    assert "@" in bio["email"]