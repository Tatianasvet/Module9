def natural_check(number):
    if type(number) is not int or number <= 0:
        raise TypeError(f'{number} — Это не натуральное число!')


def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        natural_check(res)
        d = 2
        while d < res:
            if res % d != 0:
                d += 1
            else:
                print('Составное')
                return res
        print('простое')
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    my_sum = sum([a, b, c])
    return my_sum

result = sum_three(2, 3, 6)
print(result)
