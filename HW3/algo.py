from typing import Callable
from knapsack import *
import outputtypes as out
import doctest


def greedy_value(knapsack: Knapsack, items):

    for item in sorted(items, key=Item.get_value, reverse=True):
        if knapsack.capacity >= item.weight :
            knapsack.add_item_to_knapsack(item)
        if knapsack.capacity == 0 :
            break
    return knapsack


def greedy_weight(knapsack: Knapsack, items):

    for item in sorted(items, key=Item.get_weight, reverse=False):
        if knapsack.capacity >= item.weight :
            knapsack.add_item_to_knapsack(item)
        else:
            break
    return knapsack


def greedy_ratio(knapsack: Knapsack, items):

    for item in sorted(items, key=Item.get_ratio, reverse=True):
        if knapsack.capacity >= item.weight:
            knapsack.add_item_to_knapsack(item)
        if knapsack.capacity == 0:
            break
    return knapsack


def knapsack_solver(algorithm:Callable, capacity:float, items:list, output:out.OutputType = out.Items):
    """
    :param algorithm: greedy_value, greedy_weight, greedy_ratio
    :param capacity: the knapsack capacity
    :param items: items to choose
    :param output: output format: ValuesSum, WeightSum, Items (default), TotalInfo
    :return:

    >>> items1 = [(1,2),(2,1), (3,2), (5,1), (3,1), (5,4)]
    >>> items2 = { 'a':(1, 2), 'b':(2, 1), 'c':(3, 2), 'd':(5, 1), 'e':(3, 1), 'f':(5, 4)}
    >>> knapsack_solver(algorithm= greedy_value, capacity=5, items=items1)
    [(v=5, w=1), (v=5, w=4)]
    >>> knapsack_solver(algorithm= greedy_value, capacity=5, items=items2)
    [(name=d, v=5, w=1), (name=f, v=5, w=4)]
    >>> knapsack_solver(algorithm= greedy_value, capacity=5, items=items1, output= out.ValuesSum)
    10
    >>> knapsack_solver(algorithm= greedy_value, capacity=5, items=items1, output= out.WeightSum)
    5
    >>> knapsack_solver(algorithm= greedy_value, capacity=5, items=items1, output= out.TotalInfo)
    'knapsack=[(v=5, w=1), (v=5, w=4)], value=10, weight=5'

    >>> knapsack_solver(algorithm= greedy_weight, capacity=5, items=items1)
    [(v=2, w=1), (v=5, w=1), (v=3, w=1), (v=1, w=2)]
    >>> knapsack_solver(algorithm= greedy_weight, capacity=5, items=items2)
    [(name=b, v=2, w=1), (name=d, v=5, w=1), (name=e, v=3, w=1), (name=a, v=1, w=2)]
    >>> knapsack_solver(algorithm= greedy_weight, capacity=5, items=items1, output= out.ValuesSum)
    11
    >>> knapsack_solver(algorithm= greedy_weight, capacity=5, items=items1, output= out.WeightSum)
    5
    >>> knapsack_solver(algorithm= greedy_weight, capacity=5, items=items1, output= out.TotalInfo)
    'knapsack=[(v=2, w=1), (v=5, w=1), (v=3, w=1), (v=1, w=2)], value=11, weight=5'

    >>> knapsack_solver(algorithm= greedy_ratio, capacity=5, items=items1)
    [(v=5, w=1), (v=3, w=1), (v=2, w=1), (v=3, w=2)]
    >>> knapsack_solver(algorithm= greedy_ratio, capacity=5, items=items2)
    [(name=d, v=5, w=1), (name=e, v=3, w=1), (name=b, v=2, w=1), (name=c, v=3, w=2)]
    >>> knapsack_solver(algorithm= greedy_ratio, capacity=5, items=items1, output= out.ValuesSum)
    13
    >>> knapsack_solver(algorithm= greedy_ratio, capacity=5, items=items1, output= out.WeightSum)
    5
    >>> knapsack_solver(algorithm= greedy_ratio, capacity=5, items=items1, output= out.TotalInfo)
    'knapsack=[(v=5, w=1), (v=3, w=1), (v=2, w=1), (v=3, w=2)], value=13, weight=5'
    """
    if isinstance(items, dict):  # items is a dict mapping an item_name to its (value, weight) representation.
        items = [ItemWithName(key, *value) for key, value in items.items()]
    else:  # items is a list (value, weight) representation
        items = [Item(*item) for item in items]

    knapsack = output.create_empty_knapsack(capacity)
    algorithm(knapsack, items)
    return output.extract_output_from_knapsack(knapsack)


if __name__ == '__main__':

    items1 = [(1,2),(2,1), (3,2), (5,1), (3,1), (5,4)]
    items2 = { 'a':(1, 2), 'b':(2, 1), 'c':(3, 2), 'd':(5, 1), 'e':(3, 1), 'f':(5, 4)}

    x = knapsack_solver(algorithm= greedy_ratio, capacity=5, items=items1)
    print(x)

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
