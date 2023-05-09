def main():
    from collections import deque
    n = int(input())
    adj = [[] for _ in range(9)]
    for _ in range(n):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    p = list(map(int, input().split()))
    for i in range(8):
        p[i] -= 1
    if p == [0, 1, 2, 3, 4, 5, 6, 7]:
        print(0)
        return
    q = deque()
    q.append((0, 0))
    d = [[-1]*9 for _ in range(1<<8)]
    d[0][0] = 0
    while q:
        b, u = q.popleft()
        for v in adj[u]:
            nb = b
            for i in range(8):
                if p[i] == v:
                    nb |= 1<<i
            if d[nb][v] == -1:
                d[nb][v] = d[b][u] + 1
                q.append((nb, v))
    print(min(d[(1<<8)-1]))

if __name__ == '__main__':
    main()