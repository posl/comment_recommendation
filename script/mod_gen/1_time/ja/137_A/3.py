def main():
    # A, B を取得
    A, B = map(int, input().split())
    # A + B, A - B, A * B の中で最大の数を出力
    print(max(A + B, A - B, A * B))

if __name__ == '__main__':
    main()