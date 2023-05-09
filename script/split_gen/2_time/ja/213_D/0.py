def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = [0]
    q = [0]
    while q:
        v = q.pop()
        for nv in G[v]:
            if ans[nv] == 0:
                ans[nv] = v
                q.append(nv)
    print(*[i+1 for i in ans[1:]])
