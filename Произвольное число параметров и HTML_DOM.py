def test1(*args):
    for i, arg in enumerate(args):
        print('Позиция', i, arg)


test1(2, 'привет', 3, 'бред', 55, True)


def test2(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * test2(n - 1)


print(test2(7))
