from typing import Callable
from knapsack import *
import outputtypes as out


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

    if isinstance(items, dict):  # items is a dict mapping an item to its value.
        items = [ItemWithName(key, *value) for key, value in items.items()]
    else:  # items is a list
        items = [Item(*item) for item in items]

    knapsack = output.create_empty_knapsack(capacity)
    algorithm(knapsack, items)
    return output.extract_output_from_knapsack(knapsack)


if __name__ == '__main__':

    items1 = [(1,2),(2,1), (3,2), (5,1), (3,1), (5,5)]
    items2 = { 'a':(1, 2), 'b':(2, 1), 'c':(3, 2), 'd':(5, 1), 'e':(3, 1), 'f':(5, 5)}

    x = knapsack_solver(algorithm= greedy_value, capacity=5, items=items2, output= out.Items)

    print(x)