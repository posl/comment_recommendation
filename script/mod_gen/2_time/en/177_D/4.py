def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for u in edges[v]:
                if not visited[u]:
                    stack.append(u)
    print(ans)

if __name__ == '__main__':
    main()