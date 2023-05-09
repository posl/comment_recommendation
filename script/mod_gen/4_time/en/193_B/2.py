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
    ans = 10000000000
    for i in range(N):
        if X[i] > A[i]:
            ans = min(ans, P[i])
    if ans == 10000000000:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()