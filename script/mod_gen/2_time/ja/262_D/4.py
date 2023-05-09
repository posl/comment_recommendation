def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    total = sum(A)
    ans = pow(2, N-1, MOD)
    ans *= total
    ans %= MOD
    print(ans)

if __name__ == '__main__':
    solve()