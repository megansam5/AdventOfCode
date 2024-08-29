"""Day 2: I Was Told There Would Be No Math"""


def split_string_to_length(str_length: str) -> list[int]:
    """Splits the string of lengths into a list of integers."""
    str_list = str_length.split('x')
    return [int(length) for length in str_list]


def find_surface_area(lengths: list[int]) -> int:
    """Returns the surface area plus the smallest area. """
    length = lengths[0]
    width = lengths[1]
    depth = lengths[2]
    surface_area = 2*length*width + 2*length*depth + 2*width*depth
    return surface_area + min(length*width, length*depth, width*depth)


def open_data(filename: str) -> list[str]:
    """Open the data from another file."""
    with open(filename, 'r', encoding="UTF-8") as f:
        return f.readlines()


def find_ribbon_length(lengths: list[int]) -> int:
    """Returns the smallest perimeter plus the cubic volume."""
    sorted_length = sorted(lengths)
    perimeter = 2*sorted_length[0] + 2*sorted_length[1]
    return perimeter + (sorted_length[0]*sorted_length[1]*sorted_length[2])


if __name__ == "__main__":
    data = open_data('data.txt')
    wrappings = []
    ribbon = []
    for row in data:
        wrappings.append(find_surface_area(split_string_to_length(row)))
        ribbon.append(find_ribbon_length(split_string_to_length(row)))
    print("Total wrapping:")
    print(sum(wrappings))
    print("Total ribbon:")
    print(sum(ribbon))
