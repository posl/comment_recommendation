def main():
    N, Q = map(int, input().split())
    # 隣接リストを作る
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # 頂点ごとの加算値を保存する配列
    add = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        add[p - 1] += x
    # 深さ優先探索で頂点ごとの加算値を累積する
    ans = [0] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if ans[u] == 0:
                ans[u] = ans[v] + add[u]
                stack.append(u)
    print(*ans)

if __name__ == '__main__':
    main()