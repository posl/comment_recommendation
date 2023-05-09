def main():
    N, K = map(int, input().split())
    S = input()
    # 連続するLの数とRの数をそれぞれリストに格納する
    LR = []
    LR.append(0)
    if S[0] == 'L':
        LR.append(-1)
    else:
        LR.append(1)
    for i in range(1, N):
        if S[i] == 'L':
            LR.append(LR[-1] - 1)
        else:
            LR.append(LR[-1] + 1)
    # LRを並び替えて、連続するLの数とRの数が大きい方を選ぶ
    LR.sort()
    ans = 0
    for i in range(K + 1):
        ans = max(ans, LR[-i] - LR[i])
    # 連続するLの数とRの数のうち、小さい方を選ぶ
    ans = max(ans, min(LR[-K - 1], -LR[K + 1]))
    # 答えを出力する
    print(ans)

if __name__ == '__main__':
    main()