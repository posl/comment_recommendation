def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        # i番目からスタートする
        # s: スコア
        # j: 移動回数
        s = 0
        j = 0
        # 現在地
        now = i
        # 現在地を通ったか
        passed = [0] * n
        passed[now] = 1
        while True:
            # 現在地から次の地点に移動
            now = p[now] - 1
            # 移動回数を加算
            j += 1
            # スコアを加算
            s += c[now]
            # 現在地を通ったことを記録
            passed[now] = 1
            # 現在地がスタート地点の場合
            if now == i:
                # 一周したのでループを抜ける
                break
            # 移動回数がk以下の場合
            if j <= k:
                # スコアの最大値を更新
                ans = max(ans, s)
        # 一周したので、移動回数がkを超えた場合
        if j > k:
            # 一周するまでのスコアの最大値を求める
            max_s = 0
            for i in range(n):
                if passed[i] == 0:
                    continue
                max_s += c[i]
            # 一周するまでのスコアの最大値が0以下の場合
            if max_s <= 0:
                continue
            # 一周するまでのスコアの最大値が0より大きい場合
            else:
                # 一周するまでのスコアの最大値を、k回の移動で一周するまでのスコアの最大値として計算

if __name__ == '__main__':
    main()