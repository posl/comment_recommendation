def main():
    N, M, Q = map(int, input().split())
    # 荷物の大きさと価値
    wv = [list(map(int, input().split())) for _ in range(N)]
    # 箱の大きさ
    X = list(map(int, input().split()))
    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 箱の大きさでソート
    X.sort()
    # 荷物の価値でソート
    wv.sort(key=lambda x: x[1], reverse=True)
    for L, R in query:
        # 使用可能な箱を取得
        box = X[:L-1] + X[R:]
        # 箱の大きさでソート
        box.sort()
        ans = 0
        # 荷物の価値が高い順に詰めていく
        for w, v in wv:
            # 箱がなくなったら終了
            if len(box) == 0:
                break
            # 荷物を詰める箱を探す
            for i, x in enumerate(box):
                if w <= x:
                    # 荷物を詰める箱が見つかったら、箱を削除
                    ans += v
                    del box[i]
                    break
        print(ans)

if __name__ == '__main__':
    main()