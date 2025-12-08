
from typing import Dict, List, Set
from collections import defaultdict

def part1(input: List[str]) -> int:
    n = len(input)
    m = len(input[0])
    
    start_col = input[0].index('S')
    splits = 0
    beams: Set[int] = {start_col}
    
    for r in range(1, n):
        next_beams = set()
        for c in beams:
            if 0 <= c < m:
                if input[r][c] == '^':
                    splits += 1
                    if 0 <= c - 1 < m:
                        next_beams.add(c - 1)
                    if 0 <= c + 1 < m:
                        next_beams.add(c + 1)
                else:
                    next_beams.add(c)
        beams = next_beams
    
    return splits

def part2(input: List[str]) -> int:
    n = len(input)
    m = len(input[0])
    
    start_col = input[0].index('S')

    beams: Dict[int, int] = {start_col: 1}

    for r in range(1, n):
        current = defaultdict(int)
        for c, cnt in beams.items():
            if 0 <= c < m:
                current[c] += cnt

        while True:
            changed = False
            next_state = defaultdict(int)
            for c, cnt in current.items():
                if not (0 <= c < m):
                    continue
                if input[r][c] == '^':
                    left = c - 1
                    right = c + 1
                    if 0 <= left < m:
                        next_state[left] += cnt
                    if 0 <= right < m:
                        next_state[right] += cnt
                    changed = True
                else:
                    next_state[c] += cnt
            if not changed:
                current = next_state
                break
            current = next_state

        beams = dict(current)

    return sum(beams.values())

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()