def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 机Aと机Bのそれぞれの累積和を計算
    A_cumsum = [0] * (N + 1)
    B_cumsum = [0] * (M + 1)
    for i in range(N):
        A_cumsum[i + 1] = A_cumsum[i] + A[i]
    for i in range(M):
        B_cumsum[i + 1] = B_cumsum[i] + B[i]
    # 机Bの累積和から読むことができる本の冊数の最大値を計算
    ans = 0
    for i in range(M + 1):
        if B_cumsum[i] > K:
            break
        # 机Aから読むことができる本の冊数を二分探索で計算
        ok = 0
        ng = N + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A_cumsum[mid] + B_cumsum[i] <= K:
                ok = mid
            else:
                ng = mid
        ans = max(ans, i + ok)
    print(ans)
