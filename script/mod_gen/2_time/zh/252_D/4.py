def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = [0] * (2 * 10**5 + 1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, 2 * 10**5 + 1):
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // 6
        if cnt[i] >= 1:
            for j in range(i + 1, 2 * 10**5 + 1):
                ans += cnt[i] * cnt[j] * (cnt[j] - 1) // 2
    print(ans)
solve()
