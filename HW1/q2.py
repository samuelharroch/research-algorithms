import doctest


def print_sorted(x):
    """

    :param x:
    :return:
    >>> print_sorted((2,4,1))
    (1, 2, 4)
    >>> print_sorted({1, 3, 5,2, 4})
    {1, 2, 3, 4, 5}
    """
    if isinstance(x, dict):
        keys = sorted(x.keys() ,key=str)
        print ('{' ,end='')
        for key in keys:
            print(key,': ',  end='')
            print_sorted(x[key])
        print('}', end='')

    elif isinstance(x,list):

        print('[', end='')
        for element in sorted(x,key=str):
            print_sorted(element)
        print(']', end=', ')

    elif isinstance(x, set):
        sorted_set = sorted(x,key=str)
        print('{', end='')
        for element in sorted_set:
            print_sorted(element)
        print('}', end=', ')

    elif isinstance(x, tuple):
        sorted_tuple = sorted(x,key=str)
        print('(', end='')
        for element in sorted_tuple:
            print_sorted(element)
        print(')', end=', ')

    else:
        print(x, end=', ')


if __name__ == '__main__':

    a = [2,3,1,2,1]
    print_sorted(a)
    print()

    x = [1, 5, (8,4), 6 ,3,2, {"a": 5, "c": 6, "b": {1, 3, 5,2, 4}}]
    print_sorted(x)
    print()

