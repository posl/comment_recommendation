def main():
    N, M = map(int, input().split())
    S = [input().split() for _ in range(M)]
    # WAの数を記録するリスト
    WA = [0] * (N + 1)
    # ACしたかどうかを記録するリスト
    AC = [False] * (N + 1)
    for p, s in S:
        p = int(p)
        if s == "AC":
            AC[p] = True
        else:
            if not AC[p]:
                WA[p] += 1
    # ACした問題の合計
    ac_cnt = sum(AC)
    # WAした問題の合計
    wa_cnt = 0
    for i in range(1, N + 1):
        if AC[i]:
            wa_cnt += WA[i]
    print(ac_cnt, wa_cnt)

if __name__ == '__main__':
    main()