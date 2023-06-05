def dfs(u, p):
    for v in to[u]:
        if v == p:
            continue
        if mark[v] == 0:
            mark[v] = u
            dfs(v, u)
        else:
            if ans[v] == 0:
                t = u
                while t != v:
                    ans[t] = mark[t]
                    t = mark[t]
                ans[v] = mark[v]
                print("Yes")
                for i in range(1, n + 1):
                    print(ans[i])
                exit()
            else:
                continue
    return
n, m = map(int, input().split())
to = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    to[a].append(b)
    to[b].append(a)
mark = [0] * (n + 1)
ans = [0] * (n + 1)
mark[1] = -1
dfs(1, -1)
print("No")

if __name__ == '__main__':
    dfs()