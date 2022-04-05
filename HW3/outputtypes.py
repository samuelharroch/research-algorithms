"""
Define the various available output formats for a partition algorithm.
"""

from abc import ABC
from typing import Any, List
from knapsack import *


class OutputType(ABC):
    @classmethod
    def create_empty_knapsack(cls, capacity: float) -> Knapsack:
        """
        Construct and return a Bins structure. Used at the initialization phase of an algorithm.
        """
        pass

    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        """
        Return the required output from the given list of filled bins.
        """
        pass


class ValuesSum(OutputType):
    @classmethod
    def create_empty_knapsack(cls, capacity: float):
        return KnapsackSumValueAndWeight(capacity)

    # Output the sums of all the bins (but not the bins contents).
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return knapsack.sum_values


class WeightSum(OutputType):
    @classmethod
    def create_empty_knapsack(cls, capacity: float):
        return KnapsackSumValueAndWeight(capacity)

    # Output the sums of all the bins (but not the bins contents).
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return knapsack.sum_weight


class Items(OutputType):
    @classmethod
    def create_empty_knapsack(cls, capacity: float):
        return KnapsackItems(capacity)

    # Output the set of all bins.
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return knapsack.bag


########################################################## to review ###################################################

class ItemsAndSums(Items):
    # Output the set of all bins.
    @classmethod
    def extract_output_from_knapsack(cls, knapsack: Knapsack) -> Any:
        return knapsack.bag