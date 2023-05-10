def main():
    # 入力
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    # 処理
    # ボールの個数
    n = 0
    # ボールの値の合計
    s = 0
    # ボールの最小値
    min_ball = 10 ** 9 + 1
    # ボールの値の合計
    balls = []
    for query in queries:
        if query[0] == 1:
            # ボールを追加
            n += 1
            s += query[1]
            min_ball = min(min_ball, query[1])
            balls.append(query[1])
        elif query[0] == 2:
            # ボールの値を更新
            s += n * query[1]
            min_ball += query[1]
        elif query[0] == 3:
            # ボールを取り出す
            print(balls.pop(0))
            n -= 1
            if n == 0:
                min_ball = 10 ** 9 + 1
            else:
                min_ball = min(balls)

if __name__ == '__main__':
    main()