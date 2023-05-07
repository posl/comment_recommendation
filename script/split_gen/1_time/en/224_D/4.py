def main():
    M = int(input())
    adj = [[] for _ in range(9)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    p = list(map(int, input().split()))
    for i in range(8):
        p[i] -= 1
    p.append(8)
    #print(adj)
    #print(p)
    if M == 0:
        if p == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            print(0)
        else:
            print(-1)
        return
    #print(adj)
    #print(p)
    for i in range(9):
        if i not in p:
            start = i
    #print(start)
    #print(adj)
    #print(p)
    #print(start)
    q = [start]
    d = [0] * 9
    d[start] = 1
    while q:
        cur = q.pop(0)
        for nxt in adj[cur]:
            if d[nxt] == 0:
                d[nxt] = d[cur] + 1
                q.append(nxt)
    #print(d)
    #print(adj)
    #print(p)
    #print(start)
    #print(d)
    for i in range(9):
        if d[i] == 0:
            print(-1)
            return
    #print(adj)
