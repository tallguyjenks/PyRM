import pytest

from .module import multiply

# content of test_sample.py


@pytest.mark.parametrize("num1,num2,result", [(2, 2, 4), (5, 5, 25), (10, 10, 100)])
def test_module_multiply(num1, num2, result):
    assert multiply(num1, num2) == result
