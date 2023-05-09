def main():
    # 入力受け取り
    N = int(input())
    uvws = []
    for i in range(N-1):
        uvws.append(list(map(int, input().split())))
    # 隣接リスト作成
    adj_list = [[] for _ in range(N)]
    for u, v, w in uvws:
        adj_list[u-1].append((v-1, w))
        adj_list[v-1].append((u-1, w))
    # dfs
    # https://atcoder.jp/contests/abc214/submissions/25019438
    ans = 0
    stack = [(0, 0, 0)]
    while stack:
        v, p, d = stack.pop()
        ans += d
        for nv, w in adj_list[v]:
            if nv == p:
                continue
            stack.append((nv, v, max(d, w)))
    print(ans)
