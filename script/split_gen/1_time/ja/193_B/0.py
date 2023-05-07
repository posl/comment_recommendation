def main():
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
        if A[i] < X[i]:
            ans = min(ans, P[i])
    if ans == 10**10:
        ans = -1
    print(ans)
