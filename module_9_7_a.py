from time import time


def work_time(func):
    def wrapper(*args):
        start_time = time()
        res = func(*args)
        finish_time = time()
        print(f'При {args[0]} время работы {round(finish_time - start_time, 3)} сек', file=file)
        return res
    return wrapper


def natural_check(number):
    if type(number) is not int or number <= 0:
        raise TypeError(f'{number} — Это не натуральное число!')


def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        natural_check(res)
        for i in range(2, res):    #int(res ** 0.5)
            if not res % i:
                #print(f'{res} Составное')
                return res
        print(f'{res}')
        return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    return sum([a, b, c])


@work_time
def all_simple_numbers(max_number):
    for i in range(1, max_number):
        sum_three(i, 0, 0)


with open('time.txt', mode='w', encoding='utf-8') as file:
    i = 1000
    while i <= 100000:
        all_simple_numbers(i)
        i += 10000
