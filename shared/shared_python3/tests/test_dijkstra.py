import pytest

from helpers import grid, point, dijkstra

BLOCK_CHAR = '#'

def place_blocks(g:grid.Grid2D, blocks):
    for i in range(len(blocks)):
        x,y = blocks[i]
        p = point.Point2D(x,y)
        g.set_symbol(p, BLOCK_CHAR) # Blocked


@pytest.mark.parametrize(
    "blocks, size, expected",
    [   
        pytest.param([], 3, 4),
        pytest.param([(1,1)], 3, 4),
        pytest.param([], 4, 6),
        pytest.param([(1,1), (2,1)], 4, 6),
        pytest.param([], 5, 8),
        pytest.param([(0,1),(1,1),(2,1),(3,1),(1,3),(2,3),(3,3),(4,3)], 5, 16),
        pytest.param([(1,1), (2,1), (1,2)], 4, 6),
        pytest.param([], 7, 12),      
        pytest.param([(5,4),(4,2),(4,5),(3,0),(2,1),(6,3),(2,4),(1,5),(0,6),(3,3),(2,6),(5,1)], 7, 22),
    ],    
)
def test_get_least_steps(blocks:str, size:int, expected:int) -> list:
    # When:
    g = grid.Grid2D(size, size)
    place_blocks(g, blocks)

    # Then:
    assert dijkstra.get_least_steps(g, BLOCK_CHAR) == expected