def solve(n, m, x, c, a):
    ans = 10**10
    for i in range(2**n):
        cost = 0
        level = [0]*m
        for j in range(n):
            if ((i>>j)&1):
                cost += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, cost)
    if ans == 10**10:
        return -1
    else:
        return ans
n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    c.append(tmp[0])
    a.append(tmp[1:])
print(solve(n, m, x, c, a))
