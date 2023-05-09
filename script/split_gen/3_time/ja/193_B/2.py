def main():
    N = int(input())
    A, P, X = [], [], []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    minp = 10**10
    for i in range(N):
        if A[i] < X[i]:
            minp = min(minp, P[i])
    if minp == 10**10:
        print(-1)
    else:
        print(minp)
