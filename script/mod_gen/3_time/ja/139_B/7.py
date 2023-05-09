def main():
    # A:電源タップのポート数, B:未使用の差込口数
    A, B = map(int, input().split())
    # 電源タップの個数
    cnt = 1
    # 未使用の差込口数が電源タップのポート数以上になるまで
    while B >= A:
        # 未使用の差込口数を電源タップのポート数増やす
        B -= A - 1
        # 電源タップの個数をカウントアップ
        cnt += 1
    # 電源タップの個数を出力
    print(cnt)

if __name__ == '__main__':
    main()