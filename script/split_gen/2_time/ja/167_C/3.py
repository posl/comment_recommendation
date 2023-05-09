def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    #print(N, M, X)
    #print(C)
    #print(A)
    min_cost = -1
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if (i >> j) & 1 == 1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        #print(i, cost, understanding)
        if min(understanding) >= X:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)
