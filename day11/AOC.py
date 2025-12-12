from functools import lru_cache

def buiild_graph(input):
    graph = {}
    for line in input:
        node, neighbors = line.split(": ")
        graph[node] = neighbors.split()
    return graph

@lru_cache(None)
def count(start, end):
    if start == end:
        return 1
    return sum(count(nb, end) for nb in graph.get(start, []))

graph = {}
def part1():
    return count("you", "out")

def part2():
    return count("svr", "dac") * count("dac", "fft") * count("fft", "out") \
            + count("svr", "fft") * count("fft", "dac") * count("dac", "out")
    
def main():
    input = open("input.txt", "r").read().splitlines()
    global graph
    graph = buiild_graph(input)
    part1_ans = part1()
    part2_ans = part2()
    print(f"Part 1: {part1_ans}")
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()