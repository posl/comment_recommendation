def main():
    # A1, A2, A3, A4 = 100, 200, 300, 400 点問題の案の数
    A1, A2, A3, A4 = map(int, input().split())
    # コンテストを開催可能な最大回数を表す整数を出力
    print(min(A1, A2, A3, A4))

if __name__ == '__main__':
    main()