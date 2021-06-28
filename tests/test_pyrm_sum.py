"""
Testing suite for the main app module
"""
import pytest

from pyrm.pyrm import sum


@pytest.mark.parametrize("num1,num2,result", [(2, 2, 4), (5, 5, 10), (10, 10, 20)])
def test_pyrm_sum(num1, num2, result):
    """Test sum func

    Args:
        num1 (int): first number to add
        num2 (int): second number to add
        result (int): expected sum
    """
    assert sum(num1, num2) == result
