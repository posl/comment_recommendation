def main():
    # 入力
    x_1, y_1, x_2, y_2 = map(int, input().split())
    # 出力
    print(x_2 - (y_2 - y_1), y_2 + (x_2 - x_1), x_1 - (y_2 - y_1), y_1 + (x_2 - x_1))

if __name__ == '__main__':
    main()