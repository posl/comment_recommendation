def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**5 * 12 + 1
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i >> j & 1:
                cost += C[j]
                understanding = [understanding[k] + A[j][k] for k in range(M)]
        if all(understanding[k] >= X for k in range(M)):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost != 10**5 * 12 + 1 else -1)
solve()
