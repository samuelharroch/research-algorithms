
inputs = dict()


def lastcall(function):
    def wrapper(x):
        key = function.__name__
        if key in inputs and inputs[key] == x:
            return "we know the answer is " + str(function(x))
        else:
            inputs[key] = x
            return function(x)
    return wrapper


@lastcall
def f(x: int):
    return x**2


@lastcall
def f1(x: int):
    return x**3


if __name__ == '__main__':

    print(f(2))
    print(f(2))
    print(f(2))
    print(f(4))
    print(f(2))

    print(f1(2))
    print(f1(2))
    print(f1(2))
    print(f1(4))