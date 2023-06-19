def solve(n, m, x, c, a):
    ans = 10**9
    for i in range(2**n):
        sum = 0
        level = [0]*m
        for j in range(n):
            if (i >> j) & 1:
                sum += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, sum)
    if ans == 10**9:
        return -1
    else:
        return ans
n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    s = list(map(int, input().split()))
    c.append(s[0])
    a.append(s[1:])
print(solve(n, m, x, c, a))
