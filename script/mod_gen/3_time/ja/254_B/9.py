def main():
    n = int(input())
    # 1行目は1を出力
    print(1)
    # 2行目以降は、前行の1行目から1つ前の値を取得し、その値と前行の現在の値を足した値を出力
    for i in range(1, n):
        # 前行の値を取得
        a = [int(x) for x in input().split()]
        # 1行目の値は1
        print(1, end=" ")
        # 2行目以降は、前行の1行目から1つ前の値を取得し、その値と前行の現在の値を足した値を出力
        for j in range(1, i):
            print(a[j-1] + a[j], end=" ")
        # 1行目の値は1
        print(1)

if __name__ == '__main__':
    main()