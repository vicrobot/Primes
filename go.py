from timeit import timeit
T = int(input("LIMIT").rstrip())

alg2 = ''' 
def root(n):
    Root = []
    upper = int(n**0.5) + 1
    while int(upper)> 2:
        Root = [upper] + Root
        upper = int(upper**0.5) + 1
    return Root

Root = root({0})

def genp3(n):
    v = iter(range(max(primes)+1,n))
    for i in v:
        var1 = True
        for j in primes:
            if i%j==0:
                var1 = 0
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

print(timeit(stmt = alg2, number = 1))
