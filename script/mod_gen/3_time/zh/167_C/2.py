def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 100000000
    for i in range(2 ** N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(understand[k] >= X for k in range(M)):
            min_cost = min(min_cost, cost)
    if min_cost == 100000000:
        print(-1)
    else:
        print(min_cost)
main()
