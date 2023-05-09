def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for a, b in AB:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # トポロジカルソート
    ans = []
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for w in adj[v]:
                if visited[w]:
                    continue
                stack.append(w)
            ans.append(v)
    # 出力
    if len(ans) == N:
        print(*[a + 1 for a in ans])
    else:
        print(-1)

if __name__ == '__main__':
    main()