def findBurger(N,X):
    if N == 0:
        return 0
    elif X == 1:
        return 0
    elif X <= 1 + findBurger(N-1, 2**(N-1)-1):
        return findBurger(N-1, X-1)
    elif X == 2 + findBurger(N-1, 2**(N-1)-1):
        return 1 + findBurger(N-1, 2**(N-1)-1)
    elif X <= 2 + 2*findBurger(N-1, 2**(N-1)-1):
        return 1 + findBurger(N-1, X-2)
    else:
        return 1 + findBurger(N-1, 2**(N-1)-1)
N,X = input().split()
N = int(N)
X = int(X)
print(findBurger(N,X))
