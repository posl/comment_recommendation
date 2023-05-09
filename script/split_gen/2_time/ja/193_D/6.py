def get_score(cards):
    score = 0
    for i in range(1,10):
        score += i * 10 ** cards.count(str(i))
    return score
