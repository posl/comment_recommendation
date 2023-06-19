def solve(n, a):
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    return ans
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
