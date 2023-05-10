def main():
    n, m = map(int, input().split())
    # 1枚だけで全てのゲートを通過できるIDカードの枚数
    ans = 0
    # 1枚だけで全てのゲートを通過できるIDカードのリスト
    id_list = [False] * (n + 1)
    for _ in range(m):
        l, r = map(int, input().split())
        # l番目からr番目までのIDカードは1枚だけで全てのゲートを通過できる
        for i in range(l, r + 1):
            if not id_list[i]:
                ans += 1
                id_list[i] = True
    print(ans)
main()

if __name__ == '__main__':
    main()