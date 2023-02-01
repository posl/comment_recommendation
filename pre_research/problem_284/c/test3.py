#問題文
#頂点に１からNの番号が，辺に１からMの番号がついたN頂点M辺の単純無向グラフが与えられます．辺iは頂点uiと頂点viを結んでいます．グラフに含まれる連結成分の個数を求めてください．
#
#注釈
#単純無向グラフとは，単純で辺に向きのないグラフのことをいいます．
#グラフが単純であるとは，グラフが自己ループや多重辺を含まないことをいいます．
#あるグラフの部分グラフとは，元のグラフのいくつかの頂点といくつかの辺を選んでできるグラフのことをいいます．
#グラフが連結であるとは，グラフに含まれるすべての頂点同士が辺を経由して互いに行き来できることをいいます．
#連結成分とは，連結な部分グラフのうち，そのグラフを含んだより大きい連結な部分グラフが存在しないものをいいます．
#
#制約
#1 ≦ N ≦ 100
#0 ≦ M ≦ N(N - 1) / 2
#1 ≦ ui, vi ≦ N
#入力で与えられるグラフは単純
#入力される値はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる．
#N M
#u1 v1
#u2 v2
#.
#.
#.
#uM vM
#
#出力
#答えを出力せよ．
#
#入力例１
#5 3
#1 2
#1 3
#4 5
#
#出力例１
#2
#
#入力例２
#5 0
#
#出力例２
#5
#
#入力例3
#4 6
#1 2
#1 3
#1 4
#2 3
#2 4
#3 4
#
#出力例3
#1

def main():
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = list(map(int, input().split()))
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    ans = 0
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for w in G[v]:
                stack.append(w)
    print(ans)

if __name__ == '__main__':
    main()