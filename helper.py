
def isprime(x: int):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def all_primes(N):
    res = []
    n = 2
    while n < N:
        if isprime(n):
            res.append(n)
        n += 1
    return res


def prime_exponents(n, primes):
    current = 0
    result = []
    exponent = 0
    while n >= 1:
        p = primes[current]
        if n % p == 0:
            exponent += 1
            n = n / p
        else:
            result.append(exponent)
            exponent = 0

            current += 1

            if n == 1:
                return result


def prime_factors(n, primes):
    exps = prime_exponents(n, primes)
    res = []

    for (i, expo) in enumerate(exps):
        for count in range(expo):
            res.append(primes[i])
    return res


def proper_divisors_sum(n, primes_list):
    # Sum of the divisors = product of sum (divisors(pi^ai)) where pi^ai is
    # the largest power of pi dividing n (simple recurrence). It's equal
    # to Sum(pi^j), j<=ai, = pi^ (ai+1) - 1 / (pi - 1)
    exps = prime_exponents(n, primes_list)
    sum = 1
    for (i, expo) in enumerate(exps):
        if expo > 0:
            p = primes_list[i]
            sum *= (p**(expo+1) - 1) // (p - 1)
    return sum - n
