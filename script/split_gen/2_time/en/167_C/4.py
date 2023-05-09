def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10000000000
    for i in range(2**N):
        sumA = [0] * M
        sumC = 0
        for j in range(N):
            if (i >> j) & 1:
                sumC += C[j]
                for k in range(M):
                    sumA[k] += A[j][k]
        if all(x >= X for x in sumA):
            ans = min(ans, sumC)
    if ans == 10000000000:
        print(-1)
    else:
        print(ans)
