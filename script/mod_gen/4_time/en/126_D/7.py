def main():
    N = int(input())
    edge = [tuple(map(int, input().split())) for _ in range(N - 1)]
    G = [[] for _ in range(N)]
    for u, v, w in edge:
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    ans = [-1] * N
    ans[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in G[v]:
            if ans[nv] == -1:
                ans[nv] = ans[v] ^ (w % 2)
                stack.append(nv)
    print(*ans, sep='
')

if __name__ == '__main__':
    main()