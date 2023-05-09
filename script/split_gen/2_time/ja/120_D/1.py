def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)
    #print(G)
    ans = [N*(N-1)//2]
    for i in range(M-1, -1, -1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if len(G[a]) > len(G[b]):
            a, b = b, a
        #print(a, b)
        G[a].remove(b)
        G[b].remove(a)
        ans.append(ans[-1] - len(G[a]))
        for c in G[a]:
            G[c].remove(a)
            G[c].add(b)
            G[b].add(c)
        G[a] = set()
    for i in range(M, -1, -1):
        print(ans[i])
