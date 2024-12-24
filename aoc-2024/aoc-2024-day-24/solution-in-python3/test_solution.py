import pytest

import solution

input_example = "AOC-2024-Day-24_Puzzle-Input-Example.txt"
input_example_larger = "AOC-2024-Day-24_Puzzle-Input-Example-Larger.txt"
input_full = "AOC-2024-Day-24_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 4),
        pytest.param(input_example_larger, 2024),
        pytest.param(input_full, 38869984335432),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 'TODO'),
        #pytest.param(input_example_larger, 'TODO'),
        #pytest.param(input_full, 'TODO'),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
