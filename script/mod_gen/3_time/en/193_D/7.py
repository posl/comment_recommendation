def main():
    from itertools import product
    K = int(input())
    S = input()
    T = input()
    S = S[:4]
    T = T[:4]
    S = [int(s) for s in S]
    T = [int(t) for t in T]
    #print(S)
    #print(T)
    card = [K]*9
    for s in S:
        card[s-1] -= 1
    for t in T:
        card[t-1] -= 1
    #print(card)
    Takahashi = 0
    Aoki = 0
    for i in range(9):
        Takahashi += (i+1)*(10**S.count(i+1))
        Aoki += (i+1)*(10**T.count(i+1))
    #print(Takahashi)
    #print(Aoki)
    if Takahashi > Aoki:
        print(1)
        return
    else:
        win = 0
        for i in range(9):
            if card[i] == 0:
                continue
            else:
                S.append(i+1)
                for j in range(9):
                    if card[j] == 0:
                        continue
                    else:
                        T.append(j+1)
                        if (i+1)*(10**S.count(i+1)) > (j+1)*(10**T.count(j+1)):
                            win += card[i]*card[j]
                        T.pop()
                S.pop()
        #print(win)
        print(win/(9*K-8)/(9*K-9))

if __name__ == '__main__':
    main()