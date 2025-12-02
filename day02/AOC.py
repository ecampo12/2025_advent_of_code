import re

def valid_id(nums: tuple[str, str]):
    start, end = int(nums[0]), int(nums[1])
    for num in range(start, end + 1):
        val = str(num)
        mid = len(val) // 2
        if len(val) % 2 == 0 and val[:mid] == val[mid:]:
            yield num

def part1(input):
    return sum(num for r in re.findall(r'(\d+)-(\d+)', input) for num in valid_id(r))

def valid_id_pt2(nums: tuple[str, str]) -> list[int]:
    start, end = int(nums[0]), int(nums[1])
    return [num for num in range(start, end + 1) if re.fullmatch(r'(.*)\1+', str(num))]

def part2(input):
    return sum(num for r in re.findall(r'(\d+)-(\d+)', input) for num in valid_id_pt2(r))

def main():
    input = open("input.txt", "r").read()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()