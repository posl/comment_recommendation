def main():
    n = int(input())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    visited = [False] * n
    visited[0] = True
    cur = 0
    seq = [1]
    while True:
        next = None
        for nxt in adj[cur]:
            if not visited[nxt]:
                next = nxt
                break
        if next is None:
            if cur == 0:
                break
            next = seq[-2]
        visited[next] = True
        seq.append(next+1)
        cur = next
    print(' '.join(map(str, seq)))
