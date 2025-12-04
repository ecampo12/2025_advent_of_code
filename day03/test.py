import pytest
from AOC import *

# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        (["987654321111111",
"811111111111119",
"234234234234278",
"818181911112111"], 357)
    ])
def test_part1(puzzle_input, expected):
    """Test part 1 on example input."""
    assert part1(puzzle_input) == expected

# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        (["987654321111111",
"811111111111119",
"234234234234278",
"818181911112111"], 3121910778619)
    ])
def test_part2(puzzle_input, expected):
    """Test part 2 on example input."""
    assert part2(puzzle_input) == expected
