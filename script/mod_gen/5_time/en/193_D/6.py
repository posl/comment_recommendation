def solve(K, S, T):
    #print(K, S, T)
    cards = [K] * 10
    cards[0] = 0
    for i in range(4):
        cards[int(S[i])] -= 1
        cards[int(T[i])] -= 1
    #print(cards)
    p = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j and cards[i] < 2:
                continue
            cards[i] += 1
            cards[j] += 1
            #print(i, j, cards)
            score_t = 0
            for k in range(1, 10):
                score_t += k * 10 ** cards[k]
            cards[i] -= 1
            cards[j] -= 1
            #print(i, j, cards)
            cards[i] += 1
            cards[j] += 1
            score_a = 0
            for k in range(1, 10):
                score_a += k * 10 ** cards[k]
            cards[i] -= 1
            cards[j] -= 1
            #print(i, j, score_t, score_a)
            if score_t > score_a:
                if i == j:
                    p += cards[i] / (9 * K - 8) * (cards[i] - 1) / (9 * K - 9)
                else:
                    p += cards[i] / (9 * K - 8) * cards[j] / (9 * K - 9)
    return p
K = int(input())
S = input()
T = input()
print(solve(K, S, T))

if __name__ == '__main__':
    solve()