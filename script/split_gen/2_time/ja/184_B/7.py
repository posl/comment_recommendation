def calc_score(s, x):
    score = x
    for i in range(len(s)):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    return score
