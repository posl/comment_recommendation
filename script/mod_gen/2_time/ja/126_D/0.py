def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append([v - 1, w])
        G[v - 1].append([u - 1, w])
    ans = [-1] * N
    ans[0] = 0
    que = [0]
    while que:
        now = que.pop()
        for nxt, w in G[now]:
            if ans[nxt] != -1:
                continue
            ans[nxt] = ans[now] if w % 2 == 0 else 1 - ans[now]
            que.append(nxt)
    print(*ans, sep='
')

if __name__ == '__main__':
    main()