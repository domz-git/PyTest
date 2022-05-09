from unittest import result
import parameterizing_decorator
import pytest

@pytest.mark.parametrize('var1, var2, result',
[
    (5, 5, 10),
    ('Hello', ' world', 'Hello world'),
    (2.5, 2.7, 5.2)
])

def test_add(var1, var2, result):
    assert parameterizing_decorator.add(var1, var2) == result
    