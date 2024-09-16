"""Day 3: Squares With Three Sides"""


def open_data(filename: str) -> list[str]:
    """Returns the data as a list of string."""
    with open(filename, 'r', encoding='UTF-8') as f:
        return f.read().splitlines()


def three_sides(row: str) -> list[int]:
    """Returns the row of lengths as a list of ints."""
    list_of_lengths = row.split(' ')
    return [int(length) for length in list_of_lengths if length and length != ' ']


def check_valid_triangle(length: list[int]) -> bool:
    """returns true if valid triangle and false if not."""

    sorted_lengths = sorted(length)
    return sorted_lengths[0] + sorted_lengths[1] > sorted_lengths[2]


if __name__ == "__main__":
    data = open_data('data.txt')
    count = 0
    for row in data:
        lengths = three_sides(row)
        if check_valid_triangle(lengths):
            count += 1
    print(count)
