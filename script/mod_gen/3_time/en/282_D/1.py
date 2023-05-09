def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    color = [-1] * n
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for i in g[v]:
            if color[i] == -1:
                color[i] = 1 - color[v]
                stack.append(i)
    c1 = sum(color)
    c2 = n - c1
    print(c1 * c2 - m)

if __name__ == '__main__':
    main()