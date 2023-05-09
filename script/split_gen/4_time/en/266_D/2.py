def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    ans = 0
    for i in range(N):
        ans += A[i]
    for i in range(N):
        if i == 0:
            if T[i] < X[i]:
                ans -= A[i]
        else:
            if T[i] - T[i-1] < abs(X[i] - X[i-1]):
                ans -= A[i]
    print(ans)
