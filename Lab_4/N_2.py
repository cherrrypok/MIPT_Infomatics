def decorator(func):

    def wrapper(arr):
        res = func(arr)
        if res == 0:
            print('Нет')
        elif res > 10:
            print('Очень много')
        else:
            print(res)

    return wrapper


@decorator
def f(arr):
    res = 0
    for numder in arr:
        if numder % 2 == 0:
            res += 1
    return res
