def generate_joltage(input: str) -> list[int]:
    jolts = []
    for i, c in enumerate(input):
        for d in input[i+1:]:
            jolts.append(int(c+d))
    return jolts

def part1(input: list[str]) -> int:
    return sum(max(generate_joltage(line)) for line in input)

# we use a greedy algorithm with a monotonic stack to find the largest subsequence
def largest_jolt(s: str) -> int:
    to_remove = len(s) - 12
    stack = []

    for i, ch in enumerate(s):
        while to_remove > 0 and stack and stack[-1] < ch and len(stack) + len(s) - i > 12:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    return int(''.join(stack[:12]))

def part2(input: list[str]) -> int:
    return sum(largest_jolt(line) for line in input)

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()