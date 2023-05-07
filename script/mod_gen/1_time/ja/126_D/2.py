def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    ans = [0] * N
    stack = [(0, 0)]
    while stack:
        u, p = stack.pop()
        for v, w in G[u]:
            if v == p:
                continue
            ans[v] = ans[u] ^ (w % 2)
            stack.append((v, u))
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()