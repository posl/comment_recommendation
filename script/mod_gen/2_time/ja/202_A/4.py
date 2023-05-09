def main():
    # 標準入力から値を取得する
    a, b, c = map(int, input().split())
    print(21 - a - b - c)

if __name__ == '__main__':
    main()