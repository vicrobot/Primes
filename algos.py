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
print(primes)
print(len(primes))
'''.format(T, T)                       


print(timeit(stmt = alg2, number = 1))
