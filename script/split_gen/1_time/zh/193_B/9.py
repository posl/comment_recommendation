def solve():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 10**9 + 1
    flag = False
    for i in range(N):
        if X[i] > 0 and ans > P[i]:
            ans = P[i]
            flag = True
    if flag:
        print(ans)
    else:
        print(-1)
solve()
