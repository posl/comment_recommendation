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
    result = 1000000000000000000
    for i in range(N):
        if X[i] > A[i]:
            result = min(result, P[i])
    if result == 1000000000000000000:
        result = -1
    print(result)

if __name__ == '__main__':
    solve()