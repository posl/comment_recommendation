def main():
    K = int(input())
    S = input()
    T = input()
    S_card = [0] * 9
    T_card = [0] * 9
    for i in range(4):
        S_card[int(S[i])-1] += 1
        T_card[int(T[i])-1] += 1
    def score(card):
        res = 0
        for i in range(9):
            res += (i+1) * 10**card[i]
        return res
    def calc_prob(card, K):
        res = 0
        for i in range(9):
            if card[i] + 1 > K:
                continue
            card[i] += 1
            for j in range(9):
                if card[j] + 1 > K:
                    continue
                card[j] += 1
                if score(card) > score(T_card):
                    res += (K - card[i]) * (K - card[j])
                card[j] -= 1
            card[i] -= 1
        return res
    ans = calc_prob(S_card, K) / (9*K - 8) / (9*K - 9)
    print(ans)

if __name__ == '__main__':
    main()