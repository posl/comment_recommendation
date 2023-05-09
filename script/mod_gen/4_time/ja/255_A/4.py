def main():
    # 標準入力から整数値を取得する
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(2)]
    # print(r, c)
    # print(a)
    print(a[r-1][c-1])

if __name__ == '__main__':
    main()