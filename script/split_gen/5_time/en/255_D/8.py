def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # Aをソートする
    A.sort()
    # Aの累積和を計算する
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # Aの累積和の最大値
    M = S[N]
    # 各クエリに答える
    for x in X:
        # x以下の要素の個数を二分探索で求める
        ok = 0
        ng = N + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A[mid - 1] <= x:
                ok = mid
            else:
                ng = mid
        # x以下の要素の個数を求める
        k = ok
        # x以下の要素の総和を求める
        s = S[k]
        # xより大きい要素の個数を求める
        m = N - k
        # x以下の要素の総和をxに変えるのに必要な操作回数を求める
        ans = s - k * x
        # xより大きい要素の総和をxに変えるのに必要な操作回数を求める
        ans += (M - s) - m * (x + 1)
        # 出力する
        print(ans)
