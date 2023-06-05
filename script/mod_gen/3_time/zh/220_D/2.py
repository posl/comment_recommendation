def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = 998244353
    ans = [0] * 10
    ans[a[0]] = 1
    for i in range(1, n):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j + a[i]) % 10] += ans[j]
            tmp[(j + a[i]) % 10] %= m
            tmp[(j * a[i]) % 10] += ans[j]
            tmp[(j * a[i]) % 10] %= m
        ans = tmp
    for i in range(10):
        print(ans[i])
solve()
