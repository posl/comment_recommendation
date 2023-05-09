def main():
    from collections import deque
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    d = [-1]*N
    d[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for u in adj[v]:
            if d[u] != -1:
                continue
            d[u] = v
            q.append(u)
    if -1 in d[1:]:
        print('No')
    else:
        print('Yes')
        for i in d[1:]:
            print(i+1)

if __name__ == '__main__':
    main()