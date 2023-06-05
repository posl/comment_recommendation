def main():
    K = int(input())
    S = input()
    T = input()
    S = S[0:4] + T[0:4]
    T = S[4:8] + T[4:8]
    S = S.replace("#", "")
    T = T.replace("#", "")
    S = [int(i) for i in S]
    T = [int(i) for i in T]
    S.sort()
    T.sort()
    S.reverse()
    T.reverse()
    card = [K] * 9
    for i in range(4):
        card[S[i] - 1] -= 1
        card[T[i] - 1] -= 1
    score = 0
    for i in range(9):
        for j in range(9):
            if i == j:
                if card[i] >= 2:
                    score += (i + 1) * (10 ** 2)
            else:
                if card[i] >= 1 and card[j] >= 1:
                    score += (i + 1) * (10 ** 1)
                    score += (j + 1) * (10 ** 0)
    win = 0
    for i in range(9):
        for j in range(9):
            if i == j:
                if card[i] >= 2:
                    card[i] -= 2
                    for k in range(9):
                        for l in range(9):
                            if k == l:
                                if card[k] >= 2:
                                    win += 1
                            else:
                                if card[k] >= 1 and card[l] >= 1:
                                    win += 1
                    card[i] += 2
            else:
                if card[i] >= 1 and card[j] >= 1:
                    card[i] -= 1
                    card[j] -= 1
                    for k in range(9):
                        for l in range(9):
                            if k == l:
                                if card[k] >= 2:
                                    win += 1
                            else:
                                if card[k] >= 1 and card[l] >= 1:
                                    win += 1
                    card[i] += 1
                    card[j] += 1
    print(win / (9 * K - 8) / (9 * K -
