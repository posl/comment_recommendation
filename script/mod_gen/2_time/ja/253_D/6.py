def main():
    N, A, B = map(int, input().split())
    # 3の倍数の個数
    count3 = N // A
    # 5の倍数の個数
    count5 = N // B
    # 15の倍数の個数
    count15 = N // (A * B)
    # 3の倍数の合計
    sum3 = count3 * (N - N % A + A) // 2
    # 5の倍数の合計
    sum5 = count5 * (N - N % B + B) // 2
    # 15の倍数の合計
    sum15 = count15 * (N - N % (A * B) + (A * B)) // 2
    # 3の倍数でも5の倍数でもない数の合計
    print(sum3 + sum5 - sum15)

if __name__ == '__main__':
    main()