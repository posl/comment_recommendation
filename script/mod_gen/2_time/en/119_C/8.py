def main():
    # 入力
    N, A, B, C = map(int, input().split())
    l_list = [int(input()) for _ in range(N)]
    # 処理
    min_mp = 10**10
    for i in range(4**N):
        a = 0
        b = 0
        c = 0
        mp = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 1:
                if a != 0:
                    mp += 10
                a += l_list[j]
            elif (i >> (2*j)) & 3 == 2:
                if b != 0:
                    mp += 10
                b += l_list[j]
            elif (i >> (2*j)) & 3 == 3:
                if c != 0:
                    mp += 10
                c += l_list[j]
        if a != 0 and b != 0 and c != 0:
            mp += abs(a-A) + abs(b-B) + abs(c-C) - 30
            min_mp = min(min_mp, mp)
    # 出力
    print(min_mp)
main()

if __name__ == '__main__':
    main()