def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        c = stack.pop()
        for v, w in G[c]:
            if color[v] == -1:
                color[v] = (color[c] + w) % 2
                stack.append(v)
    for c in color:
        print(c)

if __name__ == '__main__':
    main()