"""
inspired by https://www.geeksforgeeks.org/python-program-to-get-all-subsets-of-given-size-of-a-set/ (code #4)
author: Samuel Harroch
"""

import doctest


def bounded_subsets(s:set, c:float):
    """
    >>> [s for s in bounded_subsets({1,2,3}, 0)]
    [[]]
    >>> [s for s in bounded_subsets({11,21,31}, 10)]
    [[]]
    >>> [s for s in bounded_subsets({1,2,3,4}, 5)]
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [4], [1, 4]]
    >>> [s for s in bounded_subsets({1,2,3}, 4)]
    [[], [1], [2], [1, 2], [3], [1, 3]]
    >>> [s for s in bounded_subsets({1,2,3}, 6)]
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    >>> [s for s in bounded_subsets({1.5, 2.5, 0.5}, 5)]
    [[], [0.5], [1.5], [0.5, 1.5], [2.5], [0.5, 2.5], [1.5, 2.5], [0.5, 1.5, 2.5]]
    """

    sets = [[]]
    yield []

    for num in s:
        temp_sets = list(sets)  # create copy of current sets because we need to append new relevant sets
                                # (avoid changes during iteration)
        for y in temp_sets:
            temp = y + [num]  # union set
            if sum(temp) <= c:
                yield temp
                sets.append(temp)


def recursive_subsets(numbers, c):
    if not numbers:
        return [[]]
    x = recursive_subsets(numbers[1:], c)
    return x + [[numbers[0]] + y for y in x if sum([numbers[0]]+y) <= c ]


if __name__ == '__main__':

    print([s for s in bounded_subsets({1.5, 2.5, 0.5}, 5)])
    print([s for s in bounded_subsets({1, 2.5, 1.5}, 5)])
    print([s for s in bounded_subsets({1, 2, 4}, 5)])

    power_generator = bounded_subsets({1, 2, 4}, 5)
    print(type(power_generator))

    print(power_generator.__next__())
    print(power_generator.__next__())
    print(power_generator.__next__())
    print(power_generator.__next__())
    print(power_generator.__next__())
    print(power_generator.__next__())

    try:
        print(power_generator.__next__())
    except StopIteration:
        print("Error - StopIteration: no more item to iterate on")

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
