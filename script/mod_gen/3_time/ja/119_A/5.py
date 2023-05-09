def main():
    # 文字列 S が入力されます。
    S = input()
    # 2019/04/30 = 20190430
    # 2019/11/01 = 20191101
    # 2019/04/30 以降の場合は、S が表す日付が 2019 年 4 月 30 日以降なら TBD、そうでなければ Heisei と出力するプログラムを書いてください。
    if int(S.replace('/', '')) <= 20190430:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    main()