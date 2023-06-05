def solve():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        max_sum = i*(2*(10**100)+i-1)//2
        min_sum = (N+1-i)*(10**100 + N+1-i+1)//2
        ans += max_sum - min_sum + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()