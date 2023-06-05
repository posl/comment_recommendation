def solve():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    ans = 10 ** 9 + 1
    for i in range(N):
        if X[i] > 0 and ans > P[i]:
            ans = P[i]
    if ans == 10 ** 9 + 1:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    solve()