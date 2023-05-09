def main():
    n, m = map(int, input().split())
    # N 枚の ID カードのうち、i 番目の ID カードがどのゲートを通過できるかを格納する
    gate = [[] for _ in range(n)]
    for _ in range(m):
        l, r = map(int, input().split())
        gate[l-1].append(r-1)
    # 1 枚の ID カードで全てのゲートを通過できるかどうかを格納する
    can_pass = [False] * n
    # 1 枚の ID カードで全てのゲートを通過できる ID カードの枚数
    cnt = 0
    for i in range(n):
        # 1 枚の ID カードで全てのゲートを通過できる ID カードの枚数を更新
        if can_pass[i]:
            cnt += 1
        # i 番目の ID カードが通過できるゲートを更新
        for j in gate[i]:
            can_pass[j] = True
    print(cnt)

if __name__ == '__main__':
    main()