def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    S = sum(A)
    ans = 0
    for i in range(N):
        ans += A[i] * (S - A[i])
    print(ans // 2 % MOD)

if __name__ == '__main__':
    solve()