def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, A[i + M] - A[i] + sum(range(1, M + 1)) * A[i])
    print(ans)
