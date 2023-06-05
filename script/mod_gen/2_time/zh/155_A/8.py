def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += (p[i] + 1) / 2
    cur = ans
    for i in range(K, N):
        cur += (p[i] + 1) / 2
        cur -= (p[i - K] + 1) / 2
        ans = max(ans, cur)
    print(ans)

if __name__ == '__main__':
    solve()