def main():
    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和
    sum_A = [0]
    for i in range(N):
        sum_A.append(sum_A[i] + A[i])
    # 3箇所で切る
    # 3箇所の位置を固定する
    ans = float("inf")
    for i in range(1, N-1):
        for j in range(i+1, N):
            # 3箇所の位置を固定して、それぞれの総和を求める
            P = sum_A[i]
            Q = sum_A[j] - sum_A[i]
            R = sum_A[N] - sum_A[j]
            # 最大値と最小値の差の絶対値を求める
            ans = min(ans, max(P, Q, R) - min(P, Q, R))
    # 出力
    print(ans)

if __name__ == '__main__':
    main()