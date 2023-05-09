def solve():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    sum = 0
    for i in range(2, N + 2):
        sum += i
        if i >= K:
            ans += sum - (i - K) - 1
            ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()