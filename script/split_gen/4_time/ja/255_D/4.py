def main():
    #入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    #処理
    #累積和
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    #累積和の最大値
    maxB = max(B)
    #累積和の最小値
    minB = min(B)
    #累積和の最大値と最小値の差
    maxminB = maxB - minB
    #結果
    for i in range(Q):
        #X[i]と累積和の最大値と最小値の差が同じなら
        if X[i] == maxminB:
            print(maxB)
        #X[i]と累積和の最大値と最小値の差が異なるなら
        else:
            print(maxB + X[i] - maxminB)
