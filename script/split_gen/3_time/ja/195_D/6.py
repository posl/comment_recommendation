def main():
    N, M, Q = map(int, input().split())
    # 荷物の大きさと価値
    wv = [list(map(int, input().split())) for _ in range(N)]
    # 箱の大きさ
    x = list(map(int, input().split()))
    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 箱の大きさでソート
    x.sort()
    # クエリごとに処理
    for l, r in query:
        # 箱の大きさを取得
        x_tmp = x[:l-1] + x[r:]
        # 荷物の大きさと価値でソート
        wv.sort(key=lambda x: x[1], reverse=True)
        # 箱の大きさでソート
        x_tmp.sort()
        # 箱に入れられる荷物の価値の合計
        ans = 0
        # 荷物を箱に入れる
        for w, v in wv:
            for i in range(len(x_tmp)):
                # 箱に入れられる荷物の大きさより小さい場合
                if x_tmp[i] >= w:
                    # 箱に荷物を入れる
                    x_tmp[i] = -1
                    ans += v
                    break
        print(ans)
