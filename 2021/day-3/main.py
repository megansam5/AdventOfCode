"""Day 3: Binary Diagnostics"""


def read_input(filename: str) -> list[str]:
    """Reads the file as a list"""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def most_common(lst: list):
    """Returns the most common element of a list."""
    return max(set(lst), key=lst.count)


def get_list_from_index(index: int, lst: list) -> list:
    """Gets the element as an index for a list."""
    return [row[index] for row in lst]


def get_gamma_ray(data: list[str]):
    """Returns the gamma ay of the list."""
    result = ""
    binary_length = len(data[0]) - 1
    for i in range(binary_length):
        index_list = get_list_from_index(i, data)
        most_common_digit = most_common(index_list)
        result += most_common_digit
    return result


def get_epsilon_rate(gamma: str) -> str:
    """Returns the epsilon rate from the gamma ray"""
    result = ""
    for digit in gamma:
        if digit == '1':
            result += '0'
        else:
            result += '1'
    return result


def multiply_rates(gamma: str, epsilon: str) -> int:
    """Multiplies the two binary numbers."""
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    binary = read_input('data.txt')
    gamma_ray = get_gamma_ray(binary)
    epsilon_rate = get_epsilon_rate(gamma_ray)

    print(multiply_rates(gamma_ray, epsilon_rate))
