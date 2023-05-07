def main():
    N, Q = map(int, input().split())
    # 隣接リストを作る
    adj_list = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
    # 各頂点の深さを記録する
    depth = [-1]*N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj_list[v]:
            if depth[w] != -1:
                continue
            depth[w] = depth[v] + 1
            stack.append(w)
    # 各クエリについて、深さの差が偶数ならTown、奇数ならRoad
    for _ in range(Q):
        c, d = map(int, input().split())
        if abs(depth[c-1] - depth[d-1])%2 == 0:
            print('Town')
        else:
            print('Road')
