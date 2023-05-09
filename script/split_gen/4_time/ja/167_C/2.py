def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**6
    #bit全探索
    for i in range(2**N):
        #print(bin(i))
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        #print("cost = ", cost)
        #print("understand = ", understand)
        #print("min_cost = ", min_cost)
        if min_cost > cost and min(understand) >= X:
            min_cost = cost
    if min_cost == 10**6:
        print(-1)
    else:
        print(min_cost)
