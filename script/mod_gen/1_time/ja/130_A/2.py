def main():
    # X, A は 0 以上 9 以下の整数です。
    # X が A 未満の時 0、A 以上の時 10 を出力してください。
    # X, A = map(int, input().split())
    X, A = map(int, input().split())
    if X < A:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()