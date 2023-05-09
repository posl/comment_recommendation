def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    stack = [0]
    visited = [False] * N
    while stack:
        v = stack.pop()
        visited[v] = True
        for u in tree[v]:
            if not visited[u]:
                counter[u] += counter[v]
                stack.append(u)
    print(*counter)

if __name__ == '__main__':
    main()