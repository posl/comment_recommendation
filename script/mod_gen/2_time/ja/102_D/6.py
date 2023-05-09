def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 先頭から累積和をとる
    acc = [0]
    for a in A:
        acc.append(acc[-1] + a)
    # 3つめの切り口を固定する
    ans = float("inf")
    for i in range(3, N - 1):
        # 1つめの切り口を固定する
        for j in range(i - 2):
            # 2つめの切り口を固定する
            for k in range(j + 1, i - 1):
                # 総和を求める
                p = acc[k] - acc[j]
                q = acc[i] - acc[k]
                r = acc[N] - acc[i]
                s = acc[j]
                # 最大値と最小値の差の絶対値を求める
                ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)

if __name__ == '__main__':
    main()