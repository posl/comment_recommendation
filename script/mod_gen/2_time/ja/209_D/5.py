def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 各クエリについて
    for c, d in query:
        c -= 1
        d -= 1
        # 高橋君の距離
        dist_c = [-1] * N
        dist_c[c] = 0
        # 青木君の距離
        dist_d = [-1] * N
        dist_d[d] = 0
        # 高橋君の探索
        stack = [c]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if dist_c[u] != -1:
                    continue
                dist_c[u] = dist_c[v] + 1
                stack.append(u)
        # 青木君の探索
        stack = [d]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if dist_d[u] != -1:
                    continue
                dist_d[u] = dist_d[v] + 1
                stack.append(u)
        # 出力
        if dist_c[d] % 2 == dist_d[c] % 2:
            print("Town")
        else:
            print("Road")

if __name__ == '__main__':
    main()