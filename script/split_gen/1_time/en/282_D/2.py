def main():
    N, M = map(int, input().split())
    g = [[] for i in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    ans = 0
    for i in range(1, N + 1):
        for j in g[i]:
            if j > i:
                flag = True
                for k in g[j]:
                    if k in g[i]:
                        flag = False
                        break
                if flag:
                    ans += 1
    print(ans)
