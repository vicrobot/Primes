from timeit import timeit
T = int(input("LIMIT").rstrip())
alg5_betaTest = ''' 
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

print(timeit(alg5_betaTest, number = 1))
