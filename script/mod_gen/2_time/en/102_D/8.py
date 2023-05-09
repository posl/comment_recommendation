def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの累積和を求める
    cum = [0] * (N + 1)
    for i in range(N):
        cum[i + 1] = cum[i] + A[i]
    # 1つ目の切り口を固定する
    ans = 10 ** 10
    for i in range(1, N - 1):
        # 2つ目の切り口を固定する
        for j in range(i + 1, N):
            # 3つ目の切り口を固定する
            for k in range(j + 1, N):
                # 4つ目の切り口を固定する
                for l in range(k + 1, N):
                    # 4つの累積和の最大値と最小値の差の絶対値を求める
                    ans = min(ans, max(cum[i], cum[j] - cum[i], cum[k] - cum[j], cum[l] - cum[k], cum[N] - cum[l]) - min(cum[i], cum[j] - cum[i], cum[k] - cum[j], cum[l] - cum[k], cum[N] - cum[l]))
    print(ans)

if __name__ == '__main__':
    main()