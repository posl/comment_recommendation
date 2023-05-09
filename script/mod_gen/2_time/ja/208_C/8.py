def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    # 配る回数
    count = K // N
    # 配るお菓子の個数
    candy = K % N
    # 回数分配る
    for i in range(N):
        print(count, end="")
        # 配るお菓子の個数が残っている場合
        if candy > 0:
            # 国民番号が小さい順に配る
            if a[i] <= candy:
                print(" " + str(count + 1), end="")
                candy -= a[i]
            else:
                print(" " + str(count), end="")
        else:
            print(" " + str(count), end="")
        print()

if __name__ == '__main__':
    main()