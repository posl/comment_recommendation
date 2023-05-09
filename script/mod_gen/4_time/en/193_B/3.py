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
    min_cost = 10**9
    for i in range(N):
        if X[i] > A[i]:
            min_cost = min(min_cost, P[i])
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    solve()