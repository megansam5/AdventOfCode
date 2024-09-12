"""Day 1: No Time for a Taxicab"""


def open_data(filename: str) -> list[str]:
    """Open the data from another file."""
    with open(filename, 'r', encoding="UTF-8") as f:
        return f.readlines()


def create_one_string(data_list: list[str]) -> str:
    """Creates one string from a list (from data.txt)."""
    return "".join(data_list)


def create_list_of_instructions(data: str) -> list[str]:
    """Formats the string as a list of instructions."""
    instructions = data.split(',')
    return [instruction.strip() for instruction in instructions]


def find_new_coords(data: list[str]) -> list[int]:
    """Finds the new coordinates."""
    x = 0
    y = 0
    current_direction = 'N'
    for instruction in data:
        direction = instruction[0]
        amount = int(instruction[1:])
        current_direction = find_direction(current_direction, direction)
        if current_direction == 'N':
            y += amount
        elif current_direction == 'E':
            x += amount
        elif current_direction == 'S':
            y -= amount
        else:
            x -= amount
    return [x, y]


def coords_visted_twice(data: list[str]) -> list[int]:
    """Returns the coords of the first location visted twice."""
    visited = [[0, 0]]
    x = 0
    y = 0
    current_direction = 'N'
    for instruction in data:
        direction = instruction[0]
        amount = int(instruction[1:])
        current_direction = find_direction(current_direction, direction)
        for i in range(1, amount+1):
            if current_direction == 'N':
                y += 1
            elif current_direction == 'E':
                x += 1
            elif current_direction == 'S':
                y -= 1
            else:
                x -= 1
            new_location = [x, y]
            if new_location in visited:
                return new_location
            visited.append(new_location)


def find_distance(coords: list[int]):
    """Finds the distance of the coordinate from 0,0."""
    return abs(coords[0]) + abs(coords[1])


def find_direction(current: str, instruction: str) -> str:
    """Finds the new direction looking after the instruction."""
    new_direction_right = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    new_direction_left = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }
    if instruction == 'R':
        return new_direction_right[current]
    return new_direction_left[current]


if __name__ == "__main__":
    data = open_data('data.txt')
    data = create_one_string(data)
    data = create_list_of_instructions(data)
    # coords = find_new_coords(data)
    coords = coords_visted_twice(data)
    distance = find_distance(coords)
    print(distance)
