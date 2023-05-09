def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    #各数字の出現回数をカウント
    count = [0] * (n + 1)
    for i in range(4 * n - 1):
        count[a[i]] += 1
    #出現回数が奇数の数字を出力
    for i in range(1, n + 1):
        if count[i] % 2 == 1:
            print(i)
            break

if __name__ == '__main__':
    main()