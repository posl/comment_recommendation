def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    # print(N, M, X, C, A)
    min_cost = 10 ** 10
    for i in range(2 ** N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if min(understanding) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10 ** 10:
        print(-1)
    else:
        print(min_cost)
