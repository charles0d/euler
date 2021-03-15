
def q1():
    mult3 = ([3*i for i in range(1, 1000//3 + 1)])
    mult5 = ([5*i for i in range(1,200)])
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


def isprime(x:int):
    for i in range(2, int(x**0.5) +1):
        if x % i == 0:
            return False
    return True
    
def q3():
                
    def largest_prime_factor(x:int):
        current = int(x**0.5) + 1
        while current > 1:
            if x % current == 0 and isprime(current):
                return current
            current -= 1
        return 1
        
    print(largest_prime_factor(600851475143))
    
    
def q4():
    def is_palindrome(x:int):
        l = list(str(x))
        return l == l[::-1]

    for s in reversed(range(200,1999)):
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
    for i in range(1,101):
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
        

def prod(l):
    result = 1
    for x in l:
        result *= int(x)
    return result

def q8():
    n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    l = list(str(n))
    size = len(l)
    result = 0
    for offset in range(size - 13 + 1):
        if prod(l[offset:offset+13]) > result:
            result = prod(l[offset:offset+13])
    
    print(result)


def q9():
    # Largest a value is 332 (because 333 + 334 + 335 > 1000)
    for a in range(1,333):
        # Largest b > a, and c = 1000 - (a+b) > b => b < 500 - a/2
        for b in range(a+1, 500 - int(a/2) + 1):
            c = 1000 - (a + b)
            
            if a**2 + b**2 == c**2:
                print(a*b*c)
                return

def q10():
    result = 0
    for i in range(2,2000000):
        if isprime(i):
            result += i
        if i % 200000 == 0:
            print(i)
    print(result)

        
        
        
        
        
        



