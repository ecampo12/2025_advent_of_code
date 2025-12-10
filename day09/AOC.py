
from shapely.geometry import Polygon, box

def parse(input: list[str]) -> list[tuple[int, int]]:
    pts = []
    for line in input:
        x, y = map(int, line.split(","))
        pts.append((x, y))
    return pts

def part1(input):
    points = parse(input)
    n = len(points)
    best = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            if x1 != x2 and y1 != y2:
                area = (abs(x1 - x2) + 1)* (abs(y1 - y2) + 1)
                if area > best:
                    best = area

    return best

def part2(input: list[str]) -> int:
    points = parse(input)
    largest = 0
    poly = Polygon(points)

    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            
            subset_rect = box(min_x, min_y, max_x, max_y)

            if subset_rect.within(poly):
                area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
                
                if area > largest:
                    largest = area
    return largest

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    print(f"Part 1: {part1_ans}")
    part2_ans = part2(input)
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()