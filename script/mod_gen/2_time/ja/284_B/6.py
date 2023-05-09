def main():
    # 1行目の読み込み
    N = int(input())
    # 2行目の読み込み
    A = list(map(int, input().split()))
    # 奇数の個数をカウントする変数
    count = 0
    # 奇数の個数をカウントする
    for i in range(N):
        if A[i] % 2 != 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()