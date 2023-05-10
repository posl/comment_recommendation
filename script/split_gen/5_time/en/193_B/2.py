def solve():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 10**10
    for i in range(N):
        if X[i] > A[i]:
            ans = min(ans, P[i])
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
