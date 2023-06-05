def solve():
    n, k = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        min_sum = (i-1)*i//2
        max_sum = (2*n-i+1)*i//2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()