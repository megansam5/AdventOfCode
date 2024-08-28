"""Calculates horizontal and vertical position."""


def read_input(filename: str) -> list[str]:
    """Reads the file as a list"""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def calculate_position(data) -> int:
    """Calculates the depth and horizontal and multiplies them."""
    horizontal = 0
    depth = 0
    for row in data:
        split = row.split()
        direction = split[0]
        amount = int(split[1])
        if direction == 'forward':
            horizontal += amount
        elif direction == 'up':
            depth -= amount
        else:
            depth += amount

    return depth * horizontal


def calculate_position_with_aim(data) -> int:
    """Calculates the depth and horizontal by using the aim."""
    horizontal = 0
    depth = 0
    aim = 0
    for row in data:
        split = row.split()
        direction = split[0]
        amount = int(split[1])
        if direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
        else:
            horizontal += amount
            depth += (aim * amount)

    return depth * horizontal


if __name__ == "__main__":
    instructions = read_input("data.txt")
    print(calculate_position(instructions))
    print(calculate_position_with_aim(instructions))
