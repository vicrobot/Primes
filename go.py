from timeit import timeit
T = int(input("LIMIT").rstrip())

alg2 = ''' 
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
print(timeit(stmt = alg4, number = 1))






