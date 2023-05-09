def main():
    # 入力
    A, B, C, X = map(int, input().split())
    # 出力
    if X <= A:
        print(1)
    elif X <= B:
        print(C / (B - A + 1))
    else:
        print(0)

if __name__ == '__main__':
    main()