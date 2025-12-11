from collections import deque
import re
from typing import List, Tuple
import re
import pulp


def parse(line):
    lights = re.search(r'\[([.#]+)\]', line).group(1)
    target = 0
    for i,ch in enumerate(lights):
        if ch == '#':
            target |= (1 << i)
    buttons = [m.group(1) for m in re.finditer(r'\(([0-9,]*)\)', line)]
    button_masks = []
    for b in buttons:
        if b == '':
            button_masks.append(0)
        else:
            mask = 0
            for token in b.split(','):
                idx = int(token)
                mask |= (1 << idx)
            button_masks.append(mask)
    return len(lights), target, button_masks


def min_presses_bfs(L, target, button_masks):
    start = 0
    if start == target:
        return 0
    seen = {start}
    dq = deque([(start, 0)])
    while dq:
        state, d = dq.popleft()
        for bm in button_masks:
            ns = state ^ bm
            if ns == target:
                return d + 1
            if ns not in seen:
                seen.add(ns)
                dq.append((ns, d+1))
    return float('inf')

def part1(input):
    total = 0
    for line in input:
        L, target, button_masks = parse(line)
        presses = min_presses_bfs(L, target, button_masks)
        total += presses
    return total


def parse2(line: str) -> Tuple[List[List[int]], List[int]]:
    buttons = [m.group(1) for m in re.finditer(r'\(([0-9,]*)\)', line)]
    jmatch = re.search(r'\{([0-9,\s]+)\}', line)
    targets = [int(x) for x in jmatch.group(1).split(',')]
    L = len(targets)

    A = []
    for b in buttons:
        vec = [0]*L
        if b.strip():
            for t in b.split(','):
                vec[int(t)] += 1
        A.append(vec)
    return A, targets

def solve_machine(A, b):
    n = len(A)
    L = len(b)

    prob = pulp.LpProblem("joltage", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(n)]
    prob += pulp.lpSum(x)

    for i in range(L):
        prob += pulp.lpSum(A[j][i] * x[j] for j in range(n)) == b[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[prob.status] != "Optimal":
        return None

    return sum(int(x[j].value()) for j in range(n))

def part2(input):
    total = 0
    for _, line in enumerate(input):
        A, b = parse2(line)
        res = solve_machine(A, b)
        total += res
    return total

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    print(f"Part 1: {part1_ans}")
    part2_ans = part2(input)
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()