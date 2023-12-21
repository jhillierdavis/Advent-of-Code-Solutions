from collections import defaultdict, deque

from helpers import fileutils, grid

"""
def count_neighbours(g, cp):
    #print(f"DEBUG: cp={cp}")
    neighbours = g.get_cardinal_point_neighbours(cp)
    #print(f"DEBUG: neighbours={neighbours}")

    count = 0
    for n in neighbours:
        if g.get_symbol(n) != '#':
            count += 1
    return count
"""

def get_cardinal_point_neighbours_at_distance(g, cp, d, coords, visited, wrapping:bool=False):
    #print(f"DEBUG: d={d} {cp}")
    if d == 0:
        coords.add(cp)
        return
    
    neighbours = g.get_cardinal_point_neighbours(cp, wrapping)
    for n in neighbours:
        if (n,d) in visited:
            continue
        else:
            visited.add((n,d))

        if wrapping:
            u = g.get_unwrapped_coord(n)
            #print(f"DEBUG: n={n} u={u}")
            s = g.get_symbol(u)
        else:
            s = g.get_symbol(n)    

        if s != '#':    
            #coords.add(n)        
            get_cardinal_point_neighbours_at_distance(g, n, d -1, coords, visited, wrapping)            
    return




def count_wrapping_cardinal_point_neighbours_at_distance(g, cp, d, visit_map):
    if d == 0:        
        return 1
    
    count = 0
    neighbours = g.get_cardinal_point_neighbours(cp, True)
    for n in neighbours:
        if g.get_symbol(n) == '#':    
            continue

        key = (n,d)
        if key not in visit_map:
            value = count_wrapping_cardinal_point_neighbours_at_distance(g, n, d -1, visit_map)            
            visit_map[key] = value
            count += value
    return count

    


def solve_part1(filename, steps):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    matches = g.get_matching_symbol_coords('S')
    cp = matches[0]
    coords = set()
    visited = set()
    get_cardinal_point_neighbours_at_distance(g, cp, steps, coords, visited)
    #print(f"DEBUG: coords={coords}")
    count = len(coords)
    return count

"""
def solve_part2(filename, steps):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    matches = g.get_matching_symbol_coords('S')
    cp = matches[0]
    coords = set()
    visited_map = {}
    #get_cardinal_point_neighbours_at_distance(g, cp, steps, coords, visited, True)
    #print(f"DEBUG: coords={coords}")
    count = count_wrapping_cardinal_point_neighbours_at_distance(g, cp, steps, visited_map)
    return count
"""

def solve_part2(filename, steps):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    matches = g.get_matching_symbol_coords('S')
    cp = matches[0]
    coords = set()
    visited = set()
    #visited_map = defaultdict(int)    
    get_cardinal_point_neighbours_at_distance(g, cp, steps, coords, visited, True)
    #print(f"DEBUG: coords={coords}")
    count = len(coords)
    #print(f"DEBUG: g={g}")
    return count