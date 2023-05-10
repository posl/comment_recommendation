def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    import bisect
    def check(x):
        # x以下のペアの数がK個以上あるかどうか
        # 合計O(N log N)
        # 二分探索を使っている
        cnt = 0
        for i in range(N):
            if A[i] >= 0:
                break
            # A[i]を固定して、A[j]を二分探索で探す
            # 二分探索を使うことで、O(log N)
            # これをN回繰り返すので、合計O(N log N)
            cnt += bisect.bisect_left(A, (x + A[i] - 1) // A[i]) - i - 1
        if cnt >= K:
            return True
        else:
            return False
    # 二分探索
    # 最小値は負の数、最大値は正の数
    # 二分探索の終了条件は、最大値と最小値が隣り合った時
    l = -10 ** 18 - 1
    r = 10 ** 18 + 1
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m
    print(r)
