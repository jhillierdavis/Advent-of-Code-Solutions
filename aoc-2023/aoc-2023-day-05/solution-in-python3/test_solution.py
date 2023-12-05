import pytest

import solution

def test_adjuster():
    adjuster = solution.Adjuster(50,98,2)
    
    assert adjuster.contains_key(97) == False
    assert adjuster.contains_key(98) == True
    assert adjuster.contains_key(99) == True
    assert adjuster.contains_key(100) == False

    assert adjuster.get_value(98) == 50
    assert adjuster.get_value(99) == 51



@pytest.mark.parametrize(
    "filename,seed,location",
    [
        pytest.param('puzzle-input-example.txt', 79, 82),
        pytest.param('puzzle-input-example.txt', 14, 43),
        pytest.param('puzzle-input-example.txt', 55, 86),
        pytest.param('puzzle-input-example.txt', 13, 35),
        pytest.param('puzzle-input-full.txt', 1263068588, 4001340211),        
    ],    
)
def test_get_location_for_seed_from_filename(filename, seed, location):
    assert solution.get_location_for_seed_from_filename(filename, seed) == location


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param('puzzle-input-example.txt', 35),
        pytest.param('puzzle-input-full.txt', 199602917),
    ],    
)
def test_get_nearest_location_for_seeds_from_filename(filename, expected):
    assert solution.get_nearest_location_for_seeds_from_filename(filename) == expected