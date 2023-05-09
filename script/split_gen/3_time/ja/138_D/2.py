def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    counter = [0] * n
    for i in range(q):
        p, x = map(int, input().split())
        counter[p-1] += x
    visited = [False] * n
    visited[0] = True
    stack = [0]
    while stack:
        v = stack.pop()
        visited[v] = True
        for i in tree[v]:
            if visited[i]:
                continue
            counter[i] += counter[v]
            stack.append(i)
    print(' '.join(map(str, counter)))
