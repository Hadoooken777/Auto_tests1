import pytest



@pytest.fixture
def weathers():
    return [{
    "temperature": 22,
    "humidity": 60,
    "wind_speed": 5
}]


def test_temp_0(weathers):
    assert weathers["temperature"] >= 0

def test_range(weathers):
    assert 0 <= weathers["humidity"] <= 100

def test_wind(weathers):
    assert weathers["wind_speed"] < 20

