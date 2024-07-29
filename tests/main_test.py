# import pytest
from src.main import add_numbers, subtract_numbers


def test_add_numbers():
    """
    Test the `add_numbers` function by asserting that the sum of two numbers is equal to 4.

    This test case verifies that the `add_numbers` function correctly adds two numbers together
    and returns the expected result. It takes two parameters `a` and `b`, which are the numbers
    to be added. The function asserts that the sum of `a` and `b` is equal to 4.

    Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.

    Returns:
        None

    Raises:
        AssertionError: If the sum of `a` and `b` is not equal to 4.
    """
    assert add_numbers(2, 2) == 4


def test_subtract_numbers():
    """
    Test the `subtract_numbers` function by asserting that the difference of two numbers is equal to the
    expected result.

    This test case verifies that the `subtract_numbers` function correctly subtracts two numbers and returns
    the expected result.
    It takes two parameters `a` and `b`, which are the numbers to be subtracted. The function asserts that
    the difference
    of `a` and `b` is equal to the expected result.

    Parameters:
        a (int or float): The minuend.
        b (int or float): The subtrahend.

    Returns:
        None

    Raises:
        AssertionError: If the difference of `a` and `b` is not equal to the expected result.
    """
    # Positive numbers
    assert subtract_numbers(5, 2) == 3, "5 - 2 should equal 3"
    assert subtract_numbers(10, 5) == 5, "10 - 5 should equal 5"
    assert subtract_numbers(15, 10) == 5, "15 - 10 should equal 5"

    # Negative numbers
    assert subtract_numbers(-5, 2) == -7, "-5 - 2 should equal -7"

    # Zero
    assert subtract_numbers(0, 0) == 0, "0 - 0 should equal 0"
    assert subtract_numbers(0, 5) == -5, "0 - 5 should equal -5"
    assert subtract_numbers(5, 0) == 5, "5 - 0 should equal 5"

    # Decimal numbers
    assert subtract_numbers(5.5, 2.5) == 3.0, "5.5 - 2.5 should equal 3.0"
    assert subtract_numbers(10.5, 5.5) == 5.0, "10.5 - 5.5 should equal 5.0"
    assert subtract_numbers(15.5, 10.5) == 5.0, "15.5 - 10.5 should equal 5.0"
