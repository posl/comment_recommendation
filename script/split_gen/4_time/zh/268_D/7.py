def dfs(i, s, n, m, t):
    if i == n:
        return s
    for j in range(m):
        if t[j] in s:
            continue
        if s[-1] == t[j][0]:
            s1 = dfs(i+1, s+t[j][1:], n, m, t)
            if s1 != -1:
                return s1
    return -1
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
t = []
for i in range(m):
    t.append(input())
print(dfs(1, s[0], n, m, t))
