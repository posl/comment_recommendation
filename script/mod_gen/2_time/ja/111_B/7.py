def main():
    N = int(input())
    # N = 111
    # N = 112
    # N = 750
    # 1桁目が1の場合
    if N % 111 == 0:
        print(N)
    # 1桁目が1以外の場合
    else:
        print((N // 111 + 1) * 111)

if __name__ == '__main__':
    main()