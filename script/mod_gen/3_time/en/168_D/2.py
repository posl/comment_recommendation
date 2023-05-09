def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    ans = [-1] * N
    ans[0] = 0
    que = [0]
    while que:
        v = que.pop()
        for u in G[v]:
            if ans[u] == -1:
                ans[u] = v
                que.append(u)
    if -1 in ans[1:]:
        print('No')
    else:
        print('Yes')
        for i in ans[1:]:
            print(i + 1)

if __name__ == '__main__':
    main()