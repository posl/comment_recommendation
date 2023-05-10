def main():
    K = int(input())
    S = input()[:-1]
    T = input()[:-1]
    cards = [K] * 9
    for c in S[:-1]:
        cards[int(c)-1] -= 1
    for c in T[:-1]:
        cards[int(c)-1] -= 1
    def score(cards):
        s = 0
        for i in range(9):
            s += (i+1) * 10**cards[i]
        return s
    def calc(cards, T):
        if len(T) == 0:
            return score(cards[4:])
        else:
            s = 0
            for i in range(9):
                if cards[i] == 0:
                    continue
                cards[i] -= 1
                s += cards[i] * calc(cards, T[1:])
                cards[i] += 1
            return s
    cards[int(S[-1])-1] -= 1
    cards[int(T[-1])-1] -= 1
    print(calc(cards, T[1:]) / (9*K-8) / (9*K-9))

if __name__ == '__main__':
    main()