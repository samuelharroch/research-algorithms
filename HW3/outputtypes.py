"""
Define the various available output formats for a knapsack problem algorithm.
"""

from abc import ABC
from typing import Any, List
from knapsack import *


class OutputType(ABC):
    @classmethod
    def create_empty_knapsack(cls, capacity: float) -> Knapsack:
        """
        Construct and return a Knapsack structure. Used at the initialization phase of an algorithm.
        """
        pass

    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        """
        Return the required output from the given knapsack.
        """
        pass


class ValuesSum(OutputType):
    @classmethod
    def create_empty_knapsack(cls, capacity: float):
        return KnapsackSumValueAndWeight(capacity)

    # Output the sums of values.
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return knapsack.sum_values


class WeightSum(OutputType):
    @classmethod
    def create_empty_knapsack(cls, capacity: float):
        return KnapsackSumValueAndWeight(capacity)

    # Output the sums of weight.
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return knapsack.sum_weight


class Items(OutputType):
    @classmethod
    def create_empty_knapsack(cls, capacity: float):
        return KnapsackItems(capacity)

    # Output the items in the knapsack.
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return knapsack.bag


class TotalInfo(Items):
    # Output the entire info (items, total value, total weight).
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return "knapsack={}, value={}, weight={}".format(knapsack.bag, knapsack.sum_values, knapsack.sum_weight)

