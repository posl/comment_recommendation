def solve(n, k, p, c):
    ans = -10**18
    for i in range(n):
        a = []
        v = i
        while True:
            v = p[v]-1
            a.append(c[v])
            if v == i:
                break
        s = sum(a)
        l = len(a)
        t = 0
        for j in range(l):
            t += a[j]
            if j+1 > k:
                break
            now = t
            if s > 0:
                e = (k-j-1)//l
                now += s*e
            ans = max(ans, now)
    return ans
n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
print(solve(n, k, p, c))
