# test_calculator.py
import pytest
from src.calculator import Calculator

class TestCalculator:
    @classmethod
    def setup_class(cls):
        cls.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 3) == -2

    def test_add_invalid_input(self):
        with pytest.raises(TypeError):
            self.calc.add("hello", 3)

    def test_subtract_invalid_input(self):
        with pytest.raises(TypeError):
            self.calc.subtract("hello", 3)
