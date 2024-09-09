"""Day 3 - Perfectly Spherical Houses in a Vacuum"""


def open_data(filename: str) -> list[str]:
    """Open the data from another file."""
    with open(filename, 'r', encoding="UTF-8") as f:
        return f.readlines()


def create_one_string(data_list: list[str]) -> str:
    """Creates one string from a list (from data.txt)."""
    return "".join(data_list)


def create_dict_of_coordinates(positions: str) -> dict:
    """Creates a dictionary of coordinates visited."""
    x = 0
    y = 0
    result = {'0,0': 1}
    for direction in positions:
        if direction == '^':
            y += 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        else:
            y -= 1
        location = f'{x},{y}'
        if location in result:
            result[location] += 1
        else:
            result[location] = 1
    return result


def create_dict_of_coords_with_robo(positions: str) -> dict:
    """Creates a dictionary of coordinates visited with robosanta."""
    normalx = 0
    normaly = 0
    robox = 0
    roboy = 0
    result = {'0,0': 1}
    normal = True
    for direction in positions:
        if normal:
            if direction == '^':
                normaly += 1
            elif direction == '>':
                normalx += 1
            elif direction == '<':
                normalx -= 1
            else:
                normaly -= 1
            location = f'{normalx},{normaly}'
            if location in result:
                result[location] += 1
            else:
                result[location] = 1
            normal = False
        else:
            if direction == '^':
                roboy += 1
            elif direction == '>':
                robox += 1
            elif direction == '<':
                robox -= 1
            else:
                roboy -= 1
            location = f'{robox},{roboy}'
            if location in result:
                result[location] += 1
            else:
                result[location] = 1
            normal = True

    return result


def count_houses(coords: dict) -> int:
    """Returns the number of different houses visited."""
    return len(coords)


if __name__ == "__main__":
    data = open_data('data.txt')
    data = create_one_string(data)
    coords = create_dict_of_coordinates(data)
    robo_coords = create_dict_of_coords_with_robo(data)
    print(count_houses(coords))
    print(count_houses(robo_coords))
