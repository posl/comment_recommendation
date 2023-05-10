def main():
    K = int(input())
    S = input()
    T = input()
    card = [K for _ in range(10)]
    card[0] = 0
    for i in range(4):
        card[int(S[i])] -= 1
        card[int(T[i])] -= 1
    def calc_score(s):
        score = 0
        for i in range(1, 10):
            score += i * 10**s[i]
        return score
    def calc_prob(card, s, t):
        prob = 0
        for i in range(1, 10):
            for j in range(1, 10):
                if i == j:
                    if card[i] < 2:
                        continue
                    card[i] -= 2
                    s[i] += 1
                    t[i] += 1
                    prob += calc_score(s) > calc_score(t)
                    card[i] += 2
                    s[i] -= 1
                    t[i] -= 1
                else:
                    if card[i] < 1 or card[j] < 1:
                        continue
                    card[i] -= 1
                    card[j] -= 1
                    s[i] += 1
                    t[j] += 1
                    prob += calc_score(s) > calc_score(t)
                    card[i] += 1
                    card[j] += 1
                    s[i] -= 1
                    t[j] -= 1
        return prob
    prob = calc_prob(card, [0 for _ in range(10)], [0 for _ in range(10)])
    print(prob / ((9*K-8)*(9*K-9)))

if __name__ == '__main__':
    main()