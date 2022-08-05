
import inspect


def f(x:int, y:float, z:int) :
        return x+y+z


def pow(x: int, y: float):
    return x**y

def safe_call(f, **kwargs):
    """

    :param f:
    :param kwargs:
    :return:
    >>> safe_call(f, y=1.1, x=1,  z=2)
    4.1
    >>> safe_call(lambda x,y,z: x+y+z, y=1.1, x=1,  z=2)
    4.1
    >>> safe_call(f, y=1.1, x=1,  z=2.1)
    raise Exception(2.1 ,'is not from type', int)
    """

    if set(inspect.getfullargspec(f).args) != set(kwargs.keys()):
        raise Exception('invalid arguments passed')

    annotations = f.__annotations__
    annotations.pop('return', 'no return')

    for arg, arg_type in annotations.items():
        if arg_type != type(kwargs[arg]):
            raise Exception(kwargs[arg] ,'is not from type', arg_type)

    return f(**kwargs)


if __name__ == '__main__':

    print(safe_call(f, y=1.1, x=1,  z=2))

    safe_call(pow, y=2.6, x=5)

    safe_call(pow, y=2.6, x=5)

    safe_call(pow, y=2.6, x=5)
