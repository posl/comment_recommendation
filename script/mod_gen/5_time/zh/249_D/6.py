def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (max(a) + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, max(a) + 1):
        for j in range(i, max(a) + 1, i):
            ans += cnt[i] * cnt[j] * (cnt[j // i])
        ans -= cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
    print(ans)

if __name__ == '__main__':
    solve()