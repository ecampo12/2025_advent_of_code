import pytest
from AOC import *

# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        ([
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
            ], 7)
    ])
def test_part1(puzzle_input, expected):
    """Test part 1 on example input."""
    assert part1(puzzle_input) == expected

# @pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("puzzle_input,expected",
    [
        ([
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
            ], 33)
    ])
def test_part2(puzzle_input, expected):
    """Test part 2 on example input."""
    assert part2(puzzle_input) == expected
