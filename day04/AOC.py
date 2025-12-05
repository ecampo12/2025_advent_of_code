directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def find_access_points(grid):
    access_points = []
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            count = 0
            if cell == ".":
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor = grid[nr][nc]
                    if neighbor == "@":
                        count += 1
            if cell == "@" and count < 4:
                access_points.append((r, c))
    return access_points

def part1(input):
    return len(find_access_points(input))

def part2(input):
    total_removed = 0
    while True:
        access_points = find_access_points(input)
        if len(access_points) == 0:
            break
        total_removed += len(access_points)
        for r, c in access_points:
            input[r] = input[r][:c] + "." + input[r][c+1:]
    return total_removed

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()