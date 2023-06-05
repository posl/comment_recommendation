def get_score(cards):
    score = 0
    for i, c in enumerate(cards):
        if c == '#':
            break
        else:
            score += (i+1)*10**(int(c)-1)
    return score
