def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**9
    for i in range(2**N):
        cost = 0
        a = [0]*M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    a[k] += A[j][k]
        if all(x >= X for x in a):
            min_cost = min(min_cost, cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)
