def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * i - sum(A[:i])
        ans -= A[i] * (N - i - 1) - sum(A[i + 1:])
    print(ans)
    return 0
