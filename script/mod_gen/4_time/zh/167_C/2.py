def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])
    min_cost = 10**9
    for i in range(2**N):
        cost = 0
        understanding = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                understanding = [understanding[k]+A[j][k] for k in range(M)]
        if min(understanding) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()