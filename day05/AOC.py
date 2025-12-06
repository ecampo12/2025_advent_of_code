def parse(input):
    ranges = []
    for line in input.split("\n\n")[0].splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    numbers = list(map(int, input.split("\n\n")[1].splitlines()))
    return ranges, numbers
    
    
def part1(input):
    ranges, numbers = parse(input)
    count = 0
    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                count += 1
                break
    return count

# since the input ranges are massive, we have to merge them first
def merge_ranges(ranges):
    ranges.sort()
    merged = []
    curr = ranges[0]

    for r in ranges[1:]:
        if r[0] <= curr[1] + 1:
            curr = (curr[0], max(curr[1], r[1]))
        else:
            merged.append(curr)
            curr = r

    merged.append(curr)
    return merged

def part2(input):
    ranges, _ = parse(input)
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)

def main():
    input = open("input.txt", "r").read()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()