def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 1 から N までの連結成分を管理する。
    # 連結成分の個数は N 以下である。
    uf = UnionFind(N)
    # 1 から N までの連結成分の個数を管理する。
    # 連結成分の個数は N 以下である。
    cnt = [1] * N
    # 1 から N までの連結成分の個数の最大値を管理する。
    # 連結成分の個数の最大値は N 以下である。
    ans = N * (N - 1) // 2
    # 1 から N までの連結成分の個数の最大値の履歴を管理する。
    # 連結成分の個数の最大値の履歴は M 以下である。
    ans_history = [ans]
    for i in range(M - 1, 0, -1):
        # 1 から N までの連結成分の個数の最大値の履歴を更新する。
        if ans_history[-1] == 0:
            ans_history.append(0)
        else:
            ans_history.append(ans_history[-1])
        # A[i] と B[i] の連結成分を統合する。
        if uf.same(A[i] - 1, B[i] - 1):
            continue
        ans -= cnt[uf.root(A[i] - 1)] * cnt[uf.root(B[i] - 1)]
        uf.unite(A[i] - 1, B[i] - 1)
        cnt[uf.root(A[i] - 1)] += cnt[uf.root(B[i] - 1)]
        # 1 から N までの連結成
