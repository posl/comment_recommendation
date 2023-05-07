def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # W 以下の重さのチーズでの最大値を求める
    # 重さの総和は W 以下なので、重さの最大値は W とする
    dp = [0] * (W + 1)
    # チーズの重さの総和は 1 から W まで試す
    for i in range(1, W + 1):
        # チーズの種類を 1 から N まで試す
        for j in range(N):
            # チーズの重さが i 以下のとき
            if i - B[j] >= 0:
                # 今までの最大値と、今回のチーズを使ったときの最大値を比べる
                dp[i] = max(dp[i], dp[i - B[j]] + A[j])
    print(dp[W])

if __name__ == '__main__':
    main()