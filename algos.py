from timeit import timeit
#coolest response:- https://codereview.stackexchange.com/a/71166/194301
#About 16000000 in 0.1 sec. My rec: 2.47 sec. Surely it'll increase.
T = int(input("Limit").rstrip())
Alg_num = int(input('Algorithm:- ').rstrip())
alg0 = '''
def genp1(n):
    for i in range(2,n):
        var1 = 1
        for j in range(2, i):
            if i%j==0:
                var1 = 0
                break
        if var1:
            yield i
l1 = list(genp1({}))

print(len(l1))
'''.format(T)


alg1 = '''
def genp2(n):                           
    upper = int(n**0.5) + 1
    if upper <= 2:
        yield 2
        return
    for i in range(upper ,n):
        var1 = True
        for j in range(2, upper):
            if j <= i:
                if i%j==0:
                    var1 = False
                    break
        if var1:
            yield i
    t = genp2(upper)
    for i in t: yield i
l2 = sorted(list(genp2({})))
print(len(l2))
'''.format(T)


alg2 = ''' 
def root(n):
    Root = []
    upper = int(n**0.5) + 1
    while int(upper)> 2:
        Root = [upper] + Root
        upper = int(upper**0.5) + 1
    return Root

Root = root({})

def genp3(n):
    for i in range(2, n):
        var1 = True
        for j in primes:
            if j>= i: continue
            if j<i:
                if i%j==0:
                    var1 = 0
                    break
        if var1: yield i

primes = [2, 3]

for i in Root+[{}]:
     primes += list(genp3(i))

primes = list(set(primes))
#print(primes)
print(len(primes))
'''.format(T, T)                       

alg3_currupt = '''
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
print(len(get_primes({})))
'''.format(T)

alg4 = ''' 
T = {0}
def root(n):
    Root = []
    upper = int(n**0.5)+1
    while int(upper)> 2:
        Root = [upper] + Root
        upper = int(upper**0.5)+1
    return Root

Root = root(T)

def genp3(n):
    v = iter(range(max(primes)+2,n, 2))
    a = []
    for i in v:
        var1 = True
        for j in primes:
            if i%j==0:
                var1 = 0
                break
        if var1: a.append(i)
        #next(v)
    return a

primes = [2,3]

for i in Root+[T]:
     primes += list(genp3(i))

#print(primes)
print(len(primes))
'''.format(T, T)

alg5 = '''                   # my best till now.
T = {0}
def root(n):
    Root = []
    upper = int(n**0.5)+1
    while int(upper)> 2:
        Root = [upper] + Root
        upper = int(upper**0.5)+1
    return Root

Root = root(T)

def genp3(n):
    v_set = set(range(max(primes)+2,n, 2))  # v_set is free of evens.
    for j in primes:
        rem = j%3
        if rem == 2:
            v_set.difference_update(range(j**2,n, 6*j), range(j**2 + 2*j,n, 6*j))
        elif rem == 1:
            v_set.difference_update(range(j**2 ,n, 6*j), range(j**2 + 4*j,n, 6*j))
        else:
            v_set.difference_update(range(j**2,n, 2*j))   # 2*j prevents even non-primes.
    return list(v_set)

primes = [2,3]

for i in Root+[T]:
     primes += genp3(i)

print(len(primes))
'''.format(T)

alg6 = """
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return primes
print(len(sieve_of_eratosthenes({})))
""".format(T)
list_alg = [alg0, alg1, alg2, alg3_currupt, alg4, alg5, alg6]
print(timeit(stmt = list_alg[Alg_num], number = 1))

