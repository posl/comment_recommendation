def main():
    # 標準入力受け取り
    n = int(input())
    a = list(map(int, input().split()))
    # 最大操作回数
    cnt = 0
    # 2で割れる回数
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            cnt += 1
    # 出力
    print(cnt)

if __name__ == '__main__':
    main()