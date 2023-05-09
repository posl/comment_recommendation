def main():
    # 標準入力からNとLを取得する
    N, L = map(int, input().split())
    # リンゴの味のリスト
    apples = []
    # リンゴの味を計算する
    for i in range(N):
        apples.append(L + i)
    # リンゴの味の総和
    total = sum(apples)
    # リンゴの味の絶対値の最小値
    min_abs = 1000000
    # リンゴの味の総和からリンゴの味を引いた絶対値の最小値を計算する
    for i in range(N):
        abs = total - apples[i]
        if abs < 0:
            abs = abs * -1
        if abs < min_abs:
            min_abs = abs
    # 答えを出力する
    print(min_abs)

if __name__ == '__main__':
    main()