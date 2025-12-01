def part1(input: list[str]) -> int:
    dial = 50
    counter = 0
    for line in input:
        step = 1 if line[0] == 'R' else -1
        dial = (dial + step * int(line[1:])) % 100
        if dial == 0:
            counter += 1
    return counter

# I couldn't think of a clever way, so we just brute force it
def part2(input: list[str]) -> int:
    dial = 50
    counter = 0
    for line in input:
        step = 1 if line[0] == 'R' else -1
        length = int(line[1:])
        dial = (dial + step * length) % 100
        counter += sum(1 for i in range(1, length + 1) if (dial - step * (length - i)) % 100 == 0)
    return counter

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()