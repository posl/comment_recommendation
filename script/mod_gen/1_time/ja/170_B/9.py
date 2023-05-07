def main():
    """
    入力を受け取り、出力を生成する
    """
    X, Y = map(int, input().split())
    if Y % 2 == 1:
        print("No")
    elif X * 4 < Y or X * 2 > Y:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()