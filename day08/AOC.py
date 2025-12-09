import itertools, heapq, math

def parse_input(input: list[str]) -> list[tuple[int,int,int]]:
    return [tuple(map(int, line.split(','))) for line in input]

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, a: int) -> int:
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True
    
def euclid(a: tuple[int,int,int], b: tuple[int,int,int]) -> float:
    return math.dist(a, b)

def part1(input: list[str], connections: int = 1000) -> int:
    points = parse_input(input)
    n = len(points)

    def edges_gen():
        for i, j in itertools.combinations(range(n), 2):
            yield (euclid(points[i], points[j]), i, j)

    k_smallest = heapq.nsmallest(connections, edges_gen(), key=lambda t: t[0])
    uf = UnionFind(n)

    for _, i, j in k_smallest:
        uf.union(i, j)

    comp_count = {}
    for i in range(n):
        r = uf.find(i)
        comp_count[r] = comp_count.get(r, 0) + 1

    sizes = sorted(comp_count.values(), reverse=True)
    while len(sizes) < 3:
        sizes.append(1)

    a, b, c = sizes[:3]
    return a * b * c

def part2(input: list[str]) -> int:
    points = parse_input(input)
    n = len(points)
    edges = []
    for i, j in itertools.combinations(range(n), 2):
        edges.append((euclid(points[i], points[j]), i, j))

    edges.sort(key=lambda t: t[0])
    uf = UnionFind(n)

    last_edge = None
    for dist, i, j in edges:
        if uf.union(i, j):
            last_edge = (dist, i, j)
            if uf.components == 1:
                break

    _, i_last, j_last = last_edge
    
    return points[i_last][0] * points[j_last][0]

def main():
    input = open("input.txt", "r").read().splitlines()
    part1_ans = part1(input)
    part2_ans = part2(input)
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()