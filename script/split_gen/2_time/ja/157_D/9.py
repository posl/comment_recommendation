def solve(N, M, K, friend, block):
    #友達関係のグラフを作成
    friend_graph = [[] for i in range(N)]
    for a, b in friend:
        friend_graph[a - 1].append(b - 1)
        friend_graph[b - 1].append(a - 1)
    #ブロック関係のグラフを作成
    block_graph = [[] for i in range(N)]
    for c, d in block:
        block_graph[c - 1].append(d - 1)
        block_graph[d - 1].append(c - 1)
    #友達候補の数を求める
    ans = [0] * N
    for i in range(N):
        #自分自身と友達関係にない人を数える
        ans[i] = N - len(friend_graph[i]) - 1
        #ブロック関係になっている人を引く
        for j in block_graph[i]:
            if j in friend_graph[i]:
                ans[i] -= 1
    return ans
