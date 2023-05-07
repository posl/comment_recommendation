def main():
    #入力
    y = int(input())
    #処理
    #西暦年を 4 で割った余りが 2 である年の 6 月に開催されます。
    #y = y + 2
    #if y % 4 == 0:
    #    y = y + 2
    #else:
    #    y = y + 4
    #y = y + (4 - y % 4)
    #y = y + (4 - y % 4) if y % 4 != 0 else y + 2
    #y = y + (4 - y % 4) if y % 4 != 0 else y + 2
    y = y + (4 - y % 4) if y % 4 != 0 else y + 2
    #出力
    print(y)

if __name__ == '__main__':
    main()