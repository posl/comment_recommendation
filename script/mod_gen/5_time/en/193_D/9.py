def main():
    k = int(input())
    s = input()
    t = input()
    # calculate the number of cards of each number
    card_num = [k] * 9
    for i in range(4):
        card_num[int(s[i]) - 1] -= 1
        card_num[int(t[i]) - 1] -= 1
    # calculate the number of cards that Takahashi wins
    win = 0
    for i in range(9):
        for j in range(9):
            # calculate the score of Takahashi
            score_t = 0
            for k in range(9):
                score_t += (k + 1) * (10 ** (card_num[k] + (k == i) + (k == j)))
            # calculate the score of Aoki
            score_a = 0
            for k in range(9):
                score_a += (k + 1) * (10 ** (card_num[k] + (k == i)))
            # Takahashi wins if the score of Takahashi is greater than that of Aoki
            if score_t > score_a:
                if i == j:
                    win += card_num[i] * (card_num[i] - 1)
                else:
                    win += card_num[i] * card_num[j]
    # calculate the probability that Takahashi wins
    print(win / ((9 * k - 8) * (9 * k - 9)))

if __name__ == '__main__':
    main()