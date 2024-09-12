"""Day 2: Bathroom Security"""


def open_data(filename: str) -> list[str]:
    """Returns the data from another file."""
    with open(filename, 'r', encoding='UTF-8') as f:
        return f.readlines()


def find_next_button(previous_num: int, instructions: str) -> int:
    """Returns the next button pressed after the instructions."""
    coords = coords_from_button(previous_num)
    x = coords[0]
    y = coords[1]
    for direction in instructions:
        if direction == 'R' and x < 3:
            x += 1
        elif direction == 'L' and x > 1:
            x -= 1
        elif direction == 'U' and y < 3:
            y += 1
        elif direction == 'D' and y > 1:
            y -= 1
    new_coords = (x, y)
    return button_from_coords(new_coords)


def coords_from_button(button: int) -> tuple[int, int]:
    """Gets the coordinates from the button."""
    button_to_coords = {
        1: (1, 3),
        2: (2, 3),
        3: (3, 3),
        4: (1, 2),
        5: (2, 2),
        6: (3, 2),
        7: (1, 1),
        8: (2, 1),
        9: (3, 1)
    }
    return button_to_coords[button]


def button_from_coords(coords: tuple[int, int]) -> int:
    """Gets the button number from the coordinates."""
    coords_to_buttons = {
        (1, 3): 1,
        (2, 3): 2,
        (3, 3): 3,
        (1, 2): 4,
        (2, 2): 5,
        (3, 2): 6,
        (1, 1): 7,
        (2, 1): 8,
        (3, 1): 9
    }
    return coords_to_buttons[coords]


def find_code(data: list[str]) -> list[int]:
    """Returns the passcode as a list."""
    result = []
    starting = 5
    for instructions in data:
        button = find_next_button(starting, instructions)
        result.append(button)
        starting = button
    return result


def list_to_int(data: list[int]) -> int:
    """returns the list of ints as one int."""
    result = "".join([str(p) for p in data])
    return int(result)


if __name__ == "__main__":
    data = open_data('data.txt')
    code = find_code(data)
    code = list_to_int(code)
    print(code)
