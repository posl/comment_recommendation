def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    ans = [0] * (N + 1)
    ans[1] = 1
    q = [1]
    while q:
        v = q.pop()
        for nv in G[v]:
            if ans[nv] == 0:
                ans[nv] = v
                q.append(nv)
    if 0 in ans[2:]:
        print('No')
    else:
        print('Yes')
        for i in range(2, N + 1):
            print(ans[i])
