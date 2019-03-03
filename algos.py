from timeit import timeit

T = int(input("Limit").rstrip())

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
def root(n):
    Root = []
    upper = int(n**0.5)+1
    while int(upper)> 2:
        Root = [upper] + Root
        upper = int(upper**0.5)+1
    return Root

Root = root({0})

def genp3(n):
    v = iter(range(max(primes)+1,n))
    for i in v:
        var1 = True
        for j in primes:
            if i%j==0:
                var1 = 0
                # now this means that i won't be divisible by j till i+j, i+2j,.. we can make a tuple(i,j) then can skip these.
                break
        if var1:
            yield i
            next(v)

primes = [2,3]

for i in Root+[{1}]:
     primes += list(genp3(i))

#print(primes)
print(len(primes))
'''.format(T, T)

alg5 = ''' 
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
    v_set = set(range(max(primes)+2,n, 2))
    for j in primes:
        v_set.difference_update(set([j*i for i in range(1,int(n/j)+1, 2)]))
    return list(v_set)

primes = [2,3]

for i in Root+[T]:
     primes += list(genp3(i))

#print(primes)
print(len(primes))
'''.format(T)

'''print(timeit(stmt = alg1, number = 1))
print(timeit(stmt = alg2, number = 1))
print(timeit(stmt = alg3_currupt, number = 1))
print(timeit(stmt = alg4, number = 1))'''
print(timeit(stmt = alg5, number = 1))














