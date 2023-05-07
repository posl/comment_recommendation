def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    if (Y - 2 * X) % 2 == 0 and (Y - 4 * X) % 2 == 0 and Y - 2 * X >= 0 and Y - 4 * X >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()