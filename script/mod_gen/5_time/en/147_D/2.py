def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(60):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        ans += cnt * (n - cnt) * (1 << i)
        ans %= 10**9+7
    print(ans)
solve()

if __name__ == '__main__':
    solve()