from timeit import timeit
T = int(input("LIMIT").rstrip())

alg5_testing = ''' 
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
    ar = []
    v_set = set(range(max(primes)+2,n, 2))
    for j in primes:
        v_set.difference_update(set(range(j,n, 2*j)))
    return list(v_set)

primes = [2,3, 5, 7]

for i in Root+[T]:
     primes += genp3(i)

#print(primes)
print(Root+[T])
'''.format(T)
print(timeit(alg5_testing, number = 1))






