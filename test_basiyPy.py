import basicPy
import pytest

@pytest.mark.number
def test_add():
    assert basicPy.add(7,3) == 10
    assert basicPy.add(7) == 9

@pytest.mark.skip(reason="testing the skip mechanism")
def test_product():
    assert basicPy.product(2, 5) == 10
    assert basicPy.product(2) == 6