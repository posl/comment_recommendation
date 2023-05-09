def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    color = [-1] * N
    stack = [(0, 0)]
    color[0] = 0
    while stack:
        u, c = stack.pop()
        for v, w in tree[u]:
            if color[v] == -1:
                color[v] = (c + w) % 2
                stack.append((v, color[v]))
    for c in color:
        print(c)

if __name__ == '__main__':
    main()