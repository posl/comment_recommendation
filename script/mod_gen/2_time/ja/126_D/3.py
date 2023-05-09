def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))
    ans = [0] * N
    stack = [(0, 0)]
    while stack:
        v, d = stack.pop()
        ans[v] = d % 2
        for u, w in G[v]:
            if ans[u] == -1:
                stack.append((u, d + w))
    print(*ans, sep='
')

if __name__ == '__main__':
    main()