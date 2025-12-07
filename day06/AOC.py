def part1(input):
    input = [line.split() for line in input]
    rotated = [" ".join(row[i] for row in reversed(input)) for i in range(len(input[0]))]
    sum = 0
    for line in rotated:
        tokens = line.split()  
        op = tokens[0]
        if op == "+":
            val = 0
        elif op == "*":
            val = 1
        for token in tokens[1:]:
            if op == "+":
                val += int(token)
            elif op == "*":
                val *= int(token)
        sum += val
        
    return sum

def part2(input):
    ops = input[-1].split()
    input = [list(line) for line in input[:-1]]
    rotated = ["".join(row[i] for row in reversed(input)) for i in range(len(input[0]))]
    sum = 0
    op = ops.pop(0)
    val = 0 if op == "+" else 1
    for line in rotated:
        if line.strip() == "":
            sum += val
            op = ops.pop(0)
            val = 0 if op == "+" else 1
            continue
        num = int(line[::-1].strip())
        if op == "+":
            val += num
        elif op == "*":
            val *= num
    sum += val
    return sum

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()