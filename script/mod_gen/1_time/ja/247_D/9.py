def main():
    N = int(input())
    for i in range(N):
        # 2 つの整数の入力
        a, b = map(int, input().split())
        # 文字列の入力
        s = input()
        # 出力
        print("{} {}".format(a+b, s))

if __name__ == '__main__':
    main()