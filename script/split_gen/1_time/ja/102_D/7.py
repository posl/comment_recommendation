def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #累積和
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i - 1]
    #総和の最大値と最小値の差の絶対値の最小値
    ans = float("inf")
    #切る位置を全探索
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                #P,Q,R,Sの計算
                P = S[i]
                Q = S[j] - S[i]
                R = S[k] - S[j]
                S_ = S[N] - S[k]
                #総和の最大値と最小値の差の絶対値の最小値を更新
                ans = min(ans, max(P, Q, R, S_) - min(P, Q, R, S_))
    #出力
    print(ans)
