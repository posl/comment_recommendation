def main():
    # 整数の入力
    N, K = map(int, input().split())
    # 文字列の入力
    #S = input()
    # 出力
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

if __name__ == '__main__':
    main()