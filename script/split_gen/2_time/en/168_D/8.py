def main():
    N, M = map(int, input().split())
    # 1-indexed
    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    # 1-indexed
    ans = [-1] * (N + 1)
    ans[1] = 1
    que = [1]
    while que:
        n = que.pop()
        for e in g[n]:
            if ans[e] == -1:
                ans[e] = n
                que.append(e)
    if -1 in ans[2:]:
        print('No')
    else:
        print('Yes')
        for a in ans[2:]:
            print(a)
