def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    X = [0] + X + [0]
    ans = 0
    for i in range(1, Q+2):
        ans += abs(X[i] - X[i-1])
        if i == 1:
            ans += abs(A[0] - X[i])
        elif i == Q+1:
            ans += abs(A[N-1] - X[i-1])
        else:
            ans += abs(A[i-2] - A[i-1])
            ans += abs(A[i-1] - X[i])
    print(ans)
