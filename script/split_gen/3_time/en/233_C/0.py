def solve():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l[0])
        A.append(l[1:])
    #print(N, X, L, A)
    #print(N, X, L, A, file=sys.stderr)
    ans = 0
    for i in range(1 << N):
        cnt = 0
        prod = 1
        for j in range(N):
            if ((i >> j) & 1):
                cnt += 1
                prod *= A[j][0]
            else:
                prod *= A[j][1]
        if (prod == X):
            ans += cnt
    print(ans)
