"""
classes of item representation, should answers to the 2 types input requirement
"""


class Item():
    """
    basic representation with value and weight
    """
    def __init__(self, value:float, weight:float):
        self.value = value
        self.weight = weight

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def get_ratio(self):
        return self.value / self.weight

    def __str__(self):
        return '(v={}, w={})'.format(self.value, self.weight)

    def __repr__(self):
        return self.__str__()


class ItemWithName(Item):
    """
    detailed representation with name of item
    """

    def __init__(self, name:str, value:float, weight:float):
        super().__init__(value, weight)
        self.name = name

    def __str__(self):
        return '(name={}, v={}, w={})'.format(self.name, self.value, self.weight)

    def __repr__(self):
        return self.__str__()


