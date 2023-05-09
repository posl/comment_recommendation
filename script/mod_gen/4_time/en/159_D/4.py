def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += cnt[i] * (cnt[i] - 1) // 2
    for i in range(1, n + 1):
        print(ans - cnt[a[i]] + 1)

if __name__ == '__main__':
    solve()