from abc import ABC, abstractmethod
from items import *


class Knapsack(ABC):
    """
    An abstract bins class.
    """

    def __init__(self, capacity: float):
        self.bag = []
        self.capacity = capacity
        self.sum_values = 0
        self.sum_weight = 0

    @abstractmethod
    def add_item_to_knapsack(self, item: Item):
        pass

    @abstractmethod
    def result(self):
        return None


class KnapsackSumValueAndWeight(Knapsack):
    """
    A bins structure that keeps track of both the sum and the entire contents of each bin.
    """

    def add_item_to_knapsack(self, item: Item):
        self.capacity -= item.weight
        self.sum_values += item.value
        self.sum_weight += item.weight

    def result(self):
        return self.sum_values, self.sum_weight


class KnapsackItems(Knapsack):
    """
    A bins structure that keeps track of both the sum and the entire contents of each bin.
    """
    def add_item_to_knapsack(self, item: Item):
        self.capacity -= item.weight
        self.bag.append(item)

    def result(self):
        return self.bag


if __name__ == '__main__':
    item = ItemWithName('gold',1,2)

    k = KnapsackItems(5)
    k.add_item_to_knapsack(item)
    print(k.result())