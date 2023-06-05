def f():
    N, X = map(int, input().split())
    bag = []
    for i in range(N):
        L = list(map(int, input().split()))
        bag.append(L[1:])
    from itertools import product
    ans = 0
    for p in product(*bag):
        if X == 1:
            if 1 in p:
                ans += 1
        else:
            if X == 0:
                continue
            else:
                prod = 1
                for i in p:
                    prod *= i
                if prod == X:
                    ans += 1
    print(ans)
    return
f()
