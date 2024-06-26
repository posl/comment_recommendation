def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    #print(C)
    #print(A)
    min_cost = 10 ** 6
    for i in range(2 ** N):
        cost = 0
        level = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all([l >= X for l in level]):
            min_cost = min(min_cost, cost)
    if min_cost == 10 ** 6:
        print(-1)
    else:
        print(min_cost)
