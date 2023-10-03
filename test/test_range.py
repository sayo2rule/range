####
from src.range_function import ranges
import pytest

def test_point():
    assert ranges([[-3, 0], [0, 4.5]]) == [0, 0]
