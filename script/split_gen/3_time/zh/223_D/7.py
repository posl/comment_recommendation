def dfs(now):
    global flg
    global ans
    if flg:
        return
    if now == n:
        flg = True
        ans = l[:]
        return
    if not used[a[now]]:
        l.append(a[now])
        used[a[now]] = True
        dfs(now + 1)
        l.pop()
        used[a[now]] = False
    if not used[b[now]]:
        l.append(b[now])
        used[b[now]] = True
        dfs(now + 1)
        l.pop()
        used[b[now]] = False
n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
used = [False] * n
ans = [0] * n
l = []
flg = False
dfs(0)
