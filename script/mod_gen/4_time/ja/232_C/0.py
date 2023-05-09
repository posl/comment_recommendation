def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    # ABのボールを結ぶひもの組み合わせを全て列挙する
    AB_comb = []
    for i in range(2**M):
        tmp = []
        for j in range(M):
            if ((i >> j) & 1):
                tmp.append(AB[j])
        AB_comb.append(tmp)
    # CDのボールを結ぶひもの組み合わせを全て列挙する
    CD_comb = []
    for i in range(2**M):
        tmp = []
        for j in range(M):
            if ((i >> j) & 1):
                tmp.append(CD[j])
        CD_comb.append(tmp)
    # ABのボールを結ぶひもの組み合わせの中で、CDのボールを結ぶひもの組み合わせと同じものがあるかを判定する
    for ab in AB_comb:
        ab = set(map(tuple, ab))
        for cd in CD_comb:
            cd = set(map(tuple, cd))
            if ab == cd:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()