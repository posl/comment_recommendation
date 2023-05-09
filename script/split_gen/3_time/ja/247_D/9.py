def main():
    # ライブラリのインポート
    import sys
    # 入力の読み込み
    N = int(sys.stdin.readline().rstrip())
    queries = []
    for i in range(N):
        queries.append(list(map(int, sys.stdin.readline().rstrip().split())))
    # ボールの数を管理する配列
    balls = [0] * (10 ** 9 + 1)
    # ボールの合計値を管理する変数
    balls_sum = 0
    # クエリを処理する
    for query in queries:
        if query[0] == 1:
            balls[query[1]] += query[2]
            balls_sum += query[1] * query[2]
        else:
            # ボールの合計値を出力する
            print(balls_sum)
            # ボールの合計値を更新する
            balls_sum -= sum(balls[:query[1]])
            # ボールの数を更新する
            balls = balls[query[1]:]
