def main():
    # 入力
    a, b = map(int, input().split())
    # 出力
    if a <= b and b <= a*6:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()