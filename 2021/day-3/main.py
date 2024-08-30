"""Day 3: Binary Diagnostics"""


def read_input(filename: str) -> list[str]:
    """Reads the file as a list"""
    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def most_common(lst: list):
    """Returns the most common element of a list."""
    if lst.count('1') == lst.count('0'):
        return '1'
    return max(set(lst), key=lst.count)


def least_common(lst: list):
    """Returns the least common element of a list."""
    if lst.count('1') == lst.count('0'):
        return '0'
    return min(set(lst), key=lst.count)


def get_list_from_index(index: int, lst: list) -> list:
    """Gets the element as an index for a list."""
    return [row[index] for row in lst]


def get_list_only_with_values(data: list[str], index: int, most_popular: str) -> list[str]:
    """Returns the list but only with the value at the index."""
    return [number for number in data if number[index] == most_popular]


def get_oxygen_generator_rating(data: list[str]):
    """Returns the oxygen generator rating."""
    binary_length = len(data[0]) - 1
    result = ""
    for i in range(binary_length):
        index_list = get_list_from_index(i, data)
        most_common_digit = most_common(index_list)
        data = get_list_only_with_values(data, i, most_common_digit)
        result += most_common_digit
    return result


def get_co2_scrubber_rating(data: list[str]):
    """Returns tCO2 scrubber rating."""
    binary_length = len(data[0]) - 1
    result = ""
    for i in range(binary_length):
        index_list = get_list_from_index(i, data)
        least_common_digit = least_common(index_list)
        data = get_list_only_with_values(data, i, least_common_digit)
        result += least_common_digit
    return result


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


def get_life_support_rating(oxygen_generator, co2_scrubber):
    return int(oxygen_generator, 2) * int(co2_scrubber, 2)


if __name__ == "__main__":
    binary = read_input('data.txt')
    gamma_ray = get_gamma_ray(binary)
    epsilon_rate = get_epsilon_rate(gamma_ray)
    oxygen = get_oxygen_generator_rating(binary)
    co2 = get_co2_scrubber_rating(binary)

    print(multiply_rates(gamma_ray, epsilon_rate))
    print(get_life_support_rating(oxygen, co2))
