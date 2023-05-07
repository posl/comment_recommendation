def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    ans = [-1]*N
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv,nw in G[v]:
            if ans[nv] == -1:
                ans[nv] = (ans[v] + nw) % 2
                q.append(nv)
    for a in ans:
        print(a)
