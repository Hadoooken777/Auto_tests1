import pytest
from sqlalchemy.testing.util import total_size


@pytest.fixture
def products():
    return [
        {"name": "Milk", "price": 1.5, "quantity": 10},
        {"name": "Bread", "price": 0.8, "quantity": 20},
        {"name": "Eggs", "price": 2.0, "quantity": 30}
    ]

def test_cost(products):
    assert all(product["price"] > 0 for product in products)

def high_cost(products):
    total_quantity = sum(product["quantity"] for product in products)
    assert total_quantity > 50

def test_prod_1(products):
     assert any(product["price"] > 2.0 for product in products)

