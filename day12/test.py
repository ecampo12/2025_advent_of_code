import pytest
from AOC import *

# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        (
    """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
    """
            , 2)
    ])
def test_part1(puzzle_input, expected):
    """Test part 1 on example input."""
    assert part1(puzzle_input) == expected

