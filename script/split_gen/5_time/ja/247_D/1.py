def main():
    # 標準入力の取得
    q = int(input())
    # リストを初期化
    L = []
    # クエリの数だけループ
    for i in range(q):
        # クエリを取得
        query = input().split()
        # クエリの種類に応じて処理を分岐
        if query[0] == "1":
            # ボールを入れる
            L.append([int(query[1]), int(query[2])])
        else:
            # ボールを取り出す
            # 取り出すボールの数を取得
            c = int(query[1])
            # 取り出すボールの数だけループ
            total = 0
            for i in range(c):
                # ボールを取り出す
                ball = L.pop(0)
                # 合計値を計算
                total += ball[0] * ball[1]
                # ボールを戻す
                ball[1] -= 1
                if ball[1] > 0:
                    L.insert(0, ball)
            # 合計値を出力
            print(total)
