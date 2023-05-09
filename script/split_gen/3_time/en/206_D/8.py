def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [x - 1 for x in A]
    # グラフの構築
    graph = [[] for _ in range(N)]
    for i in range(N//2):
        graph[A[i]].append(A[N-1-i])
        graph[A[N-1-i]].append(A[i])
    # 連結成分の構築
    group = [-1] * N
    g = 0
    for i in range(N):
        if group[i] != -1:
            continue
        group[i] = g
        stack = [i]
        while stack:
            v = stack.pop()
            for u in graph[v]:
                if group[u] == -1:
                    group[u] = g
                    stack.append(u)
        g += 1
    # 連結成分ごとに、各頂点の個数を数える
    group_size = [0] * g
    for i in range(N):
        group_size[group[i]] += 1
    # 連結成分ごとに、各頂点の出現回数を数える
    group_count = [0] * g
    for i in range(N):
        group_count[group[i]] += 1
    # 連結成分ごとに、出現回数が最大の頂点の出現回数を数える
    max_count = [0] * g
    for i in range(N):
        max_count[group[i]] = max(max_count[group[i]], group_count[i])
    # 連結成分ごとに、出現回数が最大の頂点の出現回数を引いたものを数える
    ans = 0
    for i in range(g):
        ans += group_size[i] - max_count[i]
    # 出力
    print(ans // 2)
