def main():
    # 入力
    a, b, c = map(int, input().split())
    # 処理
    if a < b and b < c or c < b and b < a:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()