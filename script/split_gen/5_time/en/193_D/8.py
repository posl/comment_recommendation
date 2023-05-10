def get_score(card):
    card = list(card)
    card.pop()
    score = 0
    for i, c in enumerate(card):
        score += int(c) * (10 ** int(c))
    return score
K = int(input())
S = input()
T = input()
cards = [K] * 10
for i in range(4):
    cards[int(S[i])] -= 1
    cards[int(T[i])] -= 1
