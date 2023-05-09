def main():
    # 入力
    N = int(input())
    # 処理
    if N % 2 == 0:
        print(N // 2)
    else:
        print((N // 2) + 1)

if __name__ == '__main__':
    main()