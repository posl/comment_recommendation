def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = n - 1 - i
    cnt = {}
    for i in range(n):
        if a[i] not in cnt:
            cnt[a[i]] = 0
        cnt[a[i]] += 1
    cnt = sorted(cnt.items(), key=lambda x: x[0])
    for i in range(len(cnt)):
        if i == 0:
            ans[0] -= cnt[i][1] - 1
        else:
            ans[0] -= cnt[i][1]
    for i in range(1, n):
        ans[i] = ans[i - 1] + cnt[i - 1][1] - 1
    print(*ans, sep='
')
solve()
