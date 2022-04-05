from abc import ABC, abstractmethod
from items import *

"""
classes of Knapsack structures 
"""


class Knapsack(ABC):
    """
    An abstract Knapsack class.
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
    A Knapsack structure that keeps track of both value and weight (capacity used).
    """

    def add_item_to_knapsack(self, item: Item):
        self.capacity -= item.weight
        self.sum_values += item.value
        self.sum_weight += item.weight

    def result(self):
        return self.sum_values, self.sum_weight


class KnapsackItems(KnapsackSumValueAndWeight):
    """
    A bins structure that keeps also the Knapsack content.
    """
    def add_item_to_knapsack(self, item: Item):
        super().add_item_to_knapsack(item)
        self.bag.append(item)

    def result(self):
        return self.bag

