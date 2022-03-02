import random
from scipy.misc import derivative


def find_root(f,a,b):
    """

    :param f:
    :param a:
    :param b:
    :return:
    >>> find_root(lambda x: x**2- 2, 1, 3)
    1.4142135623730951
    >>> find_root(lambda x: x ** 2 - 4, 1, 3)
    2.0
    >>> find_root(lambda x: x ** 2 - 16, 1, 4)
    4.0
    >>> find_root(lambda x: x ** 2 - 16, -5, -4)
    -4.0
    """
    x_n = random.uniform(a,b)

    for i in range(9):
        x_n = x_n - f(x_n)/derivative(f,x_n)

    return x_n


if __name__ == '__main__':

    print(find_root(lambda x: x**2- 2, 1, 3))

    print(find_root(lambda x: x ** 2 - 4, 1, 3))

