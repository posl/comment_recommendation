def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = float('inf')
    for i in range(2 ** N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                understanding = [u + a for u, a in zip(understanding, A[j])]
        if all(u >= X for u in understanding):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost != float('inf') else -1)
