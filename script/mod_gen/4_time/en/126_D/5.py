def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append((v, w))
        edge[v].append((u, w))
    color = [-1] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        now, c = stack.pop()
        for next, w in edge[now]:
            if color[next] == -1:
                color[next] = (c + w) % 2
                stack.append((next, color[next]))
    for c in color:
        print(c)

if __name__ == '__main__':
    main()