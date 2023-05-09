def main():
    K = int(input())
    S = input()
    T = input()
    # 1. count cards
    cards = [K] * 10
    for c in S + T:
        if c == '#':
            continue
        cards[int(c)] -= 1
    # 2. count score
    def score(hand):
        score = 0
        for i in range(1, 10):
            score += i * 10 ** hand.count(str(i))
        return score
    # 3. count win
    win = 0
    for i in range(1, 10):
        for j in range(1, 10):
            # 3-1. count cards
            cards[i] -= 1
            cards[j] -= 1
            # 3-2. count score
            score_i = score(S + str(i))
            score_j = score(T + str(j))
            # 3-3. count win
            if score_i > score_j:
                win += (cards[i] + 1) * (cards[j] + 1)
            # 3-4. return cards
            cards[i] += 1
            cards[j] += 1
    # 4. count all
    all = sum(cards) * (sum(cards) - 1)
    # 5. print answer
    print(win / all)

if __name__ == '__main__':
    main()