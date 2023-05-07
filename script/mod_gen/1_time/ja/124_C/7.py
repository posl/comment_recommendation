def main():
    S = input()
    N = len(S)
    # 前から塗っていく場合
    cnt1 = 0
    for i in range(N):
        if (i % 2 == 0 and S[i] == '1') or (i % 2 == 1 and S[i] == '0'):
            cnt1 += 1
    # 後ろから塗っていく場合
    cnt2 = 0
    for i in range(N):
        if (i % 2 == 0 and S[N - 1 - i] == '1') or (i % 2 == 1 and S[N - 1 - i] == '0'):
            cnt2 += 1
    print(min(cnt1, cnt2))

if __name__ == '__main__':
    main()