def solve(n, ss):
    ans = 100000
    for i in range(n):
        s = ss[i]
        for j in range(10):
            t = 0
            for k in range(n):
                u = (int(s[(j + k) % 10]) - int(ss[k][j]) + 10) % 10
                t = max(t, u)
            ans = min(ans, t)
    return ans
n = int(input())
ss = []
for i in range(n):
    ss.append(input())
print(solve(n, ss))
