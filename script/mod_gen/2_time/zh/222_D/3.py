def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    MOD = 998244353
    ans = 1
    for i in range(N):
        ans *= max(b[i] - a[i] + 1, 0)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    solve()