
inputs = dict()


def lastcall(function):
    def wrapper(x):
        key = function.__name__ + str(x)
        if key in inputs:
            return "we know the answer is " + str(inputs[key])
        else:
            inputs[key] = function(x)
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

    print(f1(2))
    print(f1(2))
    print(f1(2))
    print(f1(4))