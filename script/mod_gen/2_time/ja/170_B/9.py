def main():
    # 鶴と亀の数の組合せ
    # 2匹の鶴がいる場合は、4匹の亀がいる
    # 亀の数は、(足の数 - 鶴の数 * 2) / 2
    # 亀の数が0以下の場合は、鶴と亀の数の組合せは存在しない
    # 亀の数が整数でない場合は、鶴と亀の数の組合せは存在しない
    x, y = map(int, input().split())
    if x * 2 <= y <= x * 4:
        if (y - x * 2) % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()