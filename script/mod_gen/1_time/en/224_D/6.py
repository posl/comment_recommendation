def main():
    import sys
    from collections import deque
    
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    p = list(map(int, input().split()))
    p = [i - 1 for i in p]
    
    def bfs(s, t):
        q = deque()
        q.append(s)
        dist = [-1] * 9
        dist[s] = 0
        while q:
            v = q.popleft()
            if v == t:
                return dist[v]
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    q.append(nv)
        return -1
    
    def check():
        for i in range(8):
            if bfs(i, p[i]) == -1:
                return False
        return True
    
    if not check():
        print(-1)
        sys.exit()
    
    ans = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if bfs(p[i], p[j]) != -1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()