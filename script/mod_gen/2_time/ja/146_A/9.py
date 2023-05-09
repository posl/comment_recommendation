def main():
    # 標準入力から1行を取得
    s = input()
    # 辞書型で曜日を定義
    week = {"SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}
    # 辞書型で定義した曜日の値を取得
    value = week[s]
    # 今日が日曜日の場合は7日後、それ以外は7 - 今日の曜日の値
    if value == 0:
        print(7)
    else:
        print(7 - value)

if __name__ == '__main__':
    main()