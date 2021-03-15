
def q1():
    mult3 = ([3*i for i in range(1, 1000//3 + 1)])
    mult5 = ([5*i for i in range(1, 200)])
    mult = set(mult3).union(set(mult5))

    print(sum(mult))


def q2():
    fibo = [1, 2]

    while True:
        current = fibo[-1] + fibo[-2]
        if current > 4000000:
            break
        fibo.append(current)

    print(sum([n for n in fibo if n // 2 == n / 2]))


def isprime(x: int):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def q3():

    def largest_prime_factor(x: int):
        current = int(x**0.5) + 1
        while current > 1:
            if x % current == 0 and isprime(current):
                return current
            current -= 1
        return 1

    print(largest_prime_factor(600851475143))


def q4():
    def is_palindrome(x: int):
        li = list(str(x))
        return li == li[::-1]

    for s in reversed(range(200, 1999)):
        if s >= 1099:
            a = 999
        else:
            a = s - 100
        while s-a <= a:
            if is_palindrome(a*(s-a)):
                print(a*(s-a))
                return
            a -= 1
    return 'No solution'


def q5():
    # check the primes all even numbers from 1 to 40 and take the union of them
    result = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
    print(result)


def q6():
    result = 0
    for i in range(1, 101):
        for j in range(i+1, 101):
            result += 2*i*j

    print(result)


def q7():
    count = 2
    p = 3
    while count < 10001:
        p += 1
        if isprime(p):
            count += 1
    print(p)


def prod(li):
    result = 1
    for x in li:
        result *= int(x)
    return result


def q8():
    n = '7316717653133062491922511967442657474235534919493496983520312774506' \
        '3262395783180169848018694788518438586156078911294949545950173795833' \
        '1952853208805511125406987471585238630507156932909632952274430435576' \
        '6896648950445244523161731856403098711121722383113622298934233803081' \
        '3533627661428280644448664523874930358907296290491560440772390713810' \
        '5158593079608667017242712188399879790879227492190169972088809377665' \
        '7273330010533678812202354218097512545405947522435258490771167055601' \
        '3604839586446706324415722155397536978179778461740649551492908625693' \
        '2197846862248283972241375657056057490261407972968652414535100474821' \
        '6637048440319989000889524345065854122758866688116427171479924442928' \
        '2308634656748139191231628245861786645835912456652947654568284891288' \
        '3142607690042242190226710556263211111093705442175069416589604080719' \
        '8403850962455444362981230987879927244284909188845801561660979191338' \
        '7549920052406368991256071760605886116467109405077541002256983155200' \
        '05593572972571636269561882670428252483600823257530420752963450'
    number = list(n)
    size = len(number)
    result = 0
    for offset in range(size - 13 + 1):
        if prod(number[offset:offset+13]) > result:
            result = prod(number[offset:offset+13])

    print(result)


def q9():
    # Largest a value is 332 (because 333 + 334 + 335 > 1000)
    for a in range(1, 333):
        # Largest b > a, and c = 1000 - (a+b) > b => b < 500 - a/2
        for b in range(a+1, 500 - int(a/2) + 1):
            c = 1000 - (a + b)

            if a**2 + b**2 == c**2:
                print(a*b*c)
                return


def q10():
    result = 0
    for i in range(2, 2000000):
        if isprime(i):
            result += i
        if i % 200000 == 0:
            print(i)
    print(result)
