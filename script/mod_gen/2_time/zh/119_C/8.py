def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10 ** 9
    for i in range(4 ** N):
        # 0: 使わない, 1: Aに使う, 2: Bに使う, 3: Cに使う
        tmp = [0, 0, 0, 0]
        mp = 0
        for j in range(N):
            # 0: 使わない, 1: Aに使う, 2: Bに使う, 3: Cに使う
            tmp[3 & (i >> (2 * j))] += l[j]
            if 3 & (i >> (2 * j)) != 0:
                mp += 10
        if tmp[1] != 0 and tmp[2] != 0 and tmp[3] != 0:
            mp += abs(tmp[1] - A) + abs(tmp[2] - B) + abs(tmp[3] - C)
            ans = min(ans, mp)
    print(ans)

if __name__ == '__main__':
    main()