def main():
    M = int(input())
    E = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    # 連結成分分け
    G = [[] for _ in range(9)]
    for u, v in E:
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    used = [False] * 9
    def dfs(v):
        used[v] = True
        for nv in G[v]:
            if used[nv]:
                continue
            dfs(nv)
    # 連結成分の数
    connected_component = 0
    for v in range(9):
        if used[v]:
            continue
        connected_component += 1
        dfs(v)
    # 連結成分の数が 2 以上の場合は不可能
    if connected_component >= 2:
        print(-1)
        return
    # 連結成分の数が 1 の場合は可能
    # 頂点 1 にコマ 1 があるときは必ず 1 回の操作が必要
    if P[0] == 1:
        print(1)
        return
    # 連結成分の数が 1 の場合は可能
    # 頂点 1 にコマ 1 がないときは必ず 0 回の操作が必要
    print(0)
