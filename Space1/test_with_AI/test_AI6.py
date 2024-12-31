import pytest

@pytest.fixture
def products():
    return [
    {"item": "apple", "quantity": 5, "price_per_unit": 0.5},
    {"item": "bread", "quantity": 2, "price_per_unit": 1.2},
    {"item": "milk", "quantity": 1, "price_per_unit": 1.0}
]


def test_quantity(products):
     total_quant = sum(item["quantity"] for item in products)
     expected_quant = 4
     assert total_quant > expected_quant

def test_cost_less(products):
    assert any(item["price_per_unit"] <= 0.5 for item in products)

