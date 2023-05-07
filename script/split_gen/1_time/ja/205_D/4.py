def main():
    # 入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # 1, 2, 4, 8, 9, 10, 11, ... という数列を作る
    B = [1]
    for i in range(1, N+Q):
        B.append(B[i-1]+A[i-1])
    # クエリ処理
    for k in K:
        # 二分探索
        ok = 0
        ng = N+Q
        while ng-ok > 1:
            mid = (ok+ng)//2
            if B[mid] >= k:
                ng = mid
            else:
                ok = mid
        # 出力
        print(A[ok]-B[ok]+k)
