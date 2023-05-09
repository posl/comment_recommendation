def main():
    N,M,X = map(int,input().split())
    C = []
    A = []
    for i in range(N):
        c,a = map(int,input().split())
        C.append(c)
        A.append(a)
    #print(C)
    #print(A)
    #print(N,M,X)
    min_cost = 1000000
    for i in range(2**N):
        #print(bin(i))
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i >> j) & 1 == 1:
                #print(j)
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        #print(cost)
        #print(understand)
        if min(understand) >= X:
            min_cost = min(min_cost,cost)
    if min_cost == 1000000:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()