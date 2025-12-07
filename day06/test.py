import pytest
from AOC import *

# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        ([
            "123 328  51 64 ", 
            " 45 64  387 23 ", 
            "  6 98  215 314",
            "*   +   *   +  "
            ], 4277556)
    ])
def test_part1(puzzle_input, expected):
    """Test part 1 on example input."""
    assert part1(puzzle_input) == expected

# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        ([
            "123 328  51 64 ", 
            " 45 64  387 23 ", 
            "  6 98  215 314",
            "*   +   *   +  "
            ], 3263827)
    ])
def test_part2(puzzle_input, expected):
    """Test part 2 on example input."""
    assert part2(puzzle_input) == expected
