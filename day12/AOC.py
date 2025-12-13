
def is_region_valid(region: str, shapes: list[tuple[int, int]]) -> bool:
    dimensions_str, requirements_str = region.split(": ")
    width, height = dimensions_str.split("x")

    available_area = int(width) * int(height)
    required_counts = list(map(int, requirements_str.split(" ")))

    required_area = sum(count * shapes[shape_id][1] for shape_id, count in enumerate(required_counts))

    return available_area >= required_area


def part1(data: str) -> int:
    chunks = data.split("\n\n")
    shape_chunks = chunks[:-1]
    region_chunk = chunks[-1]

    shapes = []
    for chunk in shape_chunks:
        shape_lines = "".join(chunk.split("\n")[1:])
        flattened_shape = shape_lines.replace("\n", "")

        bitmask = int(flattened_shape.replace("#", "1").replace(".", "0"), 2)
        area = flattened_shape.count("#")
        shapes.append((bitmask, area))

    return sum(is_region_valid(region_line, shapes) for region_line in region_chunk.split("\n"))


def main():
    input = open("input.txt", "r").read()
    part1_ans = part1(input)
    print(f"Part 1: {part1_ans}")


if __name__ == "__main__":
    main()