def main():
    import sys
    from collections import defaultdict
    from collections import deque
    input = sys.stdin.readline
    n, m = map(int, input().split())
    d = defaultdict(set)
    for _ in range(m):
        a, b = map(int, input().split())
        d[a].add(b)
        d[b].add(a)
    visited = [False] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        q = deque([i])
        visited[i] = True
        while q:
            cur = q.popleft()
            for nxt in d[cur]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                q.append(nxt)
        cnt += 1
    print(cnt - 1)

if __name__ == '__main__':
    main()