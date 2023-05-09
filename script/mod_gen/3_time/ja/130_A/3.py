def main():
    # 入力
    X, A = map(int, input().split())
    # 出力
    if X < A:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()