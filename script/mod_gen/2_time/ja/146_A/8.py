def main():
    # 標準入力から読み込み
    s = input()
    # 標準出力に出力
    print(7 - ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"].index(s))

if __name__ == '__main__':
    main()