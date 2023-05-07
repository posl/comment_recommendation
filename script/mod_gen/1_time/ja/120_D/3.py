def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    # 連結成分ごとに分割
    visited = [False] * (N + 1)
    def dfs(v, cc):
        visited[v] = True
        cc.append(v)
        for next_v in adj[v]:
            if not visited[next_v]:
                dfs(next_v, cc)
    cc_list = []
    for v in range(1, N + 1):
        if not visited[v]:
            cc = []
            dfs(v, cc)
            cc_list.append(cc)
    # 各連結成分について、その中に含まれる頂点の個数から不便さを求める
    ans = 0
    for cc in cc_list:
        n = len(cc)
        ans += n * (n - 1) // 2
    # 橋を渡していた場合は、それぞれの連結成分の頂点の個数の積を不便さから引く
    bridge = [False] * M
    for i in range(M):
        a = A[i]
        b = B[i]
        for cc in cc_list:
            if a in cc and b in cc:
                bridge[i] = True
                break
    for i in range(M):
        if bridge[i]:
            ans -= len(cc_list[i // 2]) * len(cc_list[i // 2 + 1])
    # 橋が崩落する順番に不便さを出力
    ans_list = [ans]
    for i in range(M - 1, 0, -1):
        if bridge[i]:
            ans -= len(cc_list[i // 2]) * len(cc_list[i // 2 + 1])
        ans_list.append(ans)
    for

if __name__ == '__main__':
    main()