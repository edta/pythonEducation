import pytest
from calculator import *


class TestCalculator:

    @pytest.mark.parametrize(
        "first_argument, second_argument, result", [
            (2, 3, 5),
            (-1, -19, -20),
            (0, 0, 0)
        ]
    )
    def test_addition(self, first_argument, second_argument, result):
        assert addition(first_argument, second_argument) == result

    @pytest.mark.parametrize(
        "first_argument, second_argument, result", [
            (5, 3, 2),
            (-1, -19, 18),
            (0, 0, 0)
        ]
    )
    def test_subtraction(self, first_argument, second_argument, result):
        assert subtraction(first_argument, second_argument) == result

    @pytest.mark.parametrize(
        "first_argument, second_argument, result", [
            (2, 3, 6),
            (-2, -19, 38),
            (0, 0, 0),
            (-2, 8, -16)
        ]
    )
    def test_multiple(self, first_argument, second_argument, result):
        assert multiple(first_argument, second_argument) == result

    @pytest.mark.parametrize(
        "first_argument, second_argument, result", [
            (2, 2, 1),
            (-25, -5, 5),
            (-3, 6, -0.5)
        ]
    )
    def test_division(self, first_argument, second_argument, result):
        assert division(first_argument, second_argument) == result
