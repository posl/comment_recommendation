def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    S = sum(A)
    ans = 0
    for i in range(N):
        S -= A[i]
        ans += A[i] * S
        ans %= MOD
    print(ans)
