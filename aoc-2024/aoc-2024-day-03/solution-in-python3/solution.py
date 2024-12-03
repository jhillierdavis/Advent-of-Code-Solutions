from helpers import fileutils

import re

def find_repeating_multiplication(text):
    pattern = re.compile(r'(mul\(\d+,\d+\))+?')
    matches = pattern.findall(text)
    return matches

def get_multiplication(snippet):
    x,y = snippet[4:-1].split(',')
    return int(x) * int(y)

def solve_part1(filename):
    text = open(filename).read().strip()

    count = 0
    matches = find_repeating_multiplication(text)
    for m in matches:
        #print(f"DEBUG: m={m}")
        count += get_multiplication(m)

    return count


def solve_part2(filename):
    text = open(filename).read().strip()

    pattern = re.compile(r'mul\(\d+,\d+\)')

    count = 0    
    enabled = True
    for i in range(len(text)):
        if text[i:].startswith('do()'):
            enabled = True
            i += 3
            continue
        elif text[i:].startswith("don't()"):
            enabled = False
            i += 6
            continue

        match = pattern.match(text[i:])
        if match is not None and enabled:
            count += get_multiplication(match.group(0))

    return count