def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)
    # print(N, Q)
    # print(S)
    # print(l)
    # print(r)
    # Sの1文字目からi文字目までにACが何個あるかを記録する配列
    S_ac = [0] * (N + 1)
    # Sの1文字目からi文字目までにACが何個あるかを記録する
    for i in range(1, N):
        if S[i - 1] == 'A' and S[i] == 'C':
            S_ac[i + 1] = S_ac[i] + 1
        else:
            S_ac[i + 1] = S_ac[i]
    # print(S_ac)
    # Sのl文字目からr文字目までにACが何個あるかを出力する
    for i in range(Q):
        print(S_ac[r[i]] - S_ac[l[i]])

if __name__ == '__main__':
    main()