def main():
    K = int(input())
    S = input()
    T = input()
    #print(K)
    #print(S)
    #print(T)
    Takahashi = {}
    Aoki = {}
    for i in range(1,10):
        Takahashi[i] = K
        Aoki[i] = K
    for i in range(4):
        Takahashi[int(S[i])] -= 1
        Aoki[int(T[i])] -= 1
    #print(Takahashi)
    #print(Aoki)
    Takahashi_score = 0
    Aoki_score = 0
    for i in range(1,10):
        Takahashi_score += i * 10**(Takahashi[i])
        Aoki_score += i * 10**(Aoki[i])
    #print(Takahashi_score)
    #print(Aoki_score)
    Takahashi_win = 0
    for i in range(1,10):
        if Takahashi[i] == 0:
            continue
        Takahashi[i] -= 1
        for j in range(1,10):
            if Aoki[j] == 0:
                continue
            Aoki[j] -= 1
            Takahashi_score_tmp = Takahashi_score + i * 10**(Takahashi[i]) - i * 10**(Takahashi[i]+1)
            Aoki_score_tmp = Aoki_score + j * 10**(Aoki[j]) - j * 10**(Aoki[j]+1)
            #print(Takahashi_score_tmp)
            #print(Aoki_score_tmp)
            if Takahashi_score_tmp > Aoki_score_tmp:
                Takahashi_win += Takahashi[i] + 1
            Aoki[j] += 1
        Takahashi[i] += 1
    #print(Takahashi_win)
    print(Takahashi_win / ((9*K-8)*(9*K-9)))

if __name__ == '__main__':
    main()