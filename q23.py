from helper import *


primes_list = all_primes(100000)


def is_abundant(n, primes_list):
    return proper_divisors_sum(n, primes_list) > n


def q23():

    abundants = []
    for i in range(2, 28123):
        if is_abundant(i, primes_list):
            abundants.append(i)
        if i % 3000 == 0:
            print(i)

    ab_sum = set()
    for i in abundants:
        if i > 14100:
            break
        for j in abundants:
            ab_sum.add(i+j)
        if i % 3000 == 0:
            print(i, len(ab_sum))

    print(len(ab_sum))
    ab_sum = sorted(list(ab_sum), reverse=True)
    print('sorted')

    res = []
    for i in range(1, 28124):
        if ab_sum[-1] != i:
            res.append(i)
        else:
            ab_sum.pop(-1)

    print(sum(res))


q23()
