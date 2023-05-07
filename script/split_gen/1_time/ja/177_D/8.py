def main():
    N, M = map(int, input().split())
    #友達関係を表すグラフ
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        G[B - 1].append(A - 1)
    #友達関係のグループ
    group = [-1] * N
    #グループの数
    group_num = 0
    #グループ分け
    for i in range(N):
        if group[i] != -1:
            continue
        #深さ優先探索
        stack = [i]
        while stack:
            v = stack.pop()
            group[v] = group_num
            for u in G[v]:
                if group[u] == -1:
                    stack.append(u)
        group_num += 1
    print(group_num)
