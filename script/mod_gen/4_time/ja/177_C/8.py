def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    S = 0
    for i in range(N):
        S += A[i]
        S %= MOD
    ans = 0
    for i in range(N):
        S -= A[i]
        S %= MOD
        ans += A[i]*S
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    solve()