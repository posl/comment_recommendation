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
    ans = []
    for i in range(N):
        if A[i] < X[i]:
            ans.append(P[i])
    if ans:
        print(min(ans))
    else:
        print(-1)
