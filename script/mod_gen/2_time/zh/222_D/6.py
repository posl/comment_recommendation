def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    ans = 1
    for i in range(N):
        ans = ans * max(0, B[i] - A[i] + 1) % MOD
    print(ans)
solve()
