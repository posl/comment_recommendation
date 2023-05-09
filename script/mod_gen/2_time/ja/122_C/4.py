def main():
    # 入力
    N, Q = map(int, input().split())
    S = input()
    l_r = [list(map(int, input().split())) for _ in range(Q)]
    # 前処理
    # 1文字目から順に、ACが何個現れたかを記録していく
    # 例: S = ACACTACG
    #     ac = [0, 0, 1, 1, 1, 2, 2, 2]
    ac = [0]
    for i in range(1, N):
        if S[i - 1] == "A" and S[i] == "C":
            ac.append(ac[i - 1] + 1)
        else:
            ac.append(ac[i - 1])
    # 出力
    for l, r in l_r:
        print(ac[r - 1] - ac[l - 1])

if __name__ == '__main__':
    main()