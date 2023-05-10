def main():
    K = int(input())
    S = input()[:-1]
    T = input()[:-1]
    S_cards = [0] * 9
    T_cards = [0] * 9
    S_score = 0
    T_score = 0
    for i in range(4):
        S_score += int(S[i]) * 10 ** S_cards[int(S[i]) - 1]
        S_cards[int(S[i]) - 1] += 1
        T_score += int(T[i]) * 10 ** T_cards[int(T[i]) - 1]
        T_cards[int(T[i]) - 1] += 1
    S_left = K
    T_left = K
    for i in range(9):
        S_left -= S_cards[i]
        T_left -= T_cards[i]
    win = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                if S_left < 2 or T_left < 2:
                    continue
                S_tmp = S_score + i * 10 ** S_cards[i - 1]
                T_tmp = T_score + j * 10 ** T_cards[j - 1]
                if S_tmp > T_tmp:
                    win += (S_left / (9 * K - 8)) * ((S_left - 1) / (9 * K - 9))
            else:
                if S_left < 1 or T_left < 1:
                    continue
                S_tmp = S_score + i * 10 ** S_cards[i - 1]
                T_tmp = T_score + j * 10 ** T_cards[j - 1]
                if S_tmp > T_tmp:
                    win += (S_left / (9 * K - 8)) * (T_left / (9 * K - 9))
    print(win)
