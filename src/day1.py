from typing import Iterable, Tuple

from input import get_input_filename


def find_sum_of_two(numbers: Iterable[int], wanted_sum: int, start=0
) -> Tuple[int, int]:
    """Return two numbers from `numbers` which sum up to `wanted_sum`

    If `start` is set, only look at the part of the list starting at that index
    """

    numbers = sorted(numbers)
    i = start
    j = len(numbers) - 1
    a = numbers[i]
    b = numbers[j]
    while i < j:
        if a + b < wanted_sum:
            i += 1
            a = numbers[i]
        elif a + b > wanted_sum:
            j -= 1
            b = numbers[j]
        else:
            return a, b

    raise ValueError("Sum not found")


def find_sum_of_three(numbers: Iterable[int], wanted_sum: int
) -> Tuple[int, int, int]:
    """Return three numbers from `numbers` which sum up to `wanted_sum`"""

    numbers = sorted(numbers)
    for i in range(len(numbers) - 2):
        a = numbers[i]
        try:
            b, c = find_sum_of_two(numbers, wanted_sum-a, start=i+1)
            return a, b, c
        except ValueError:
            continue

    raise ValueError("Sum not found")


with open(get_input_filename(1), 'rt') as f:
    numbers = (int(line) for line in f)
    a, b = find_sum_of_two(numbers, 2020)


print(f'Solution one: {a * b}')


with open(get_input_filename(1), 'rt') as f:
    numbers = (int(line) for line in f)
    a, b, c = find_sum_of_three(numbers, 2020)


print(f'Solution two: {a * b * c}')
