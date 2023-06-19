def countScore(N, X, S):
    score = X
    for i in range(N):
        if S[i] == 'o':
            score += 1
        elif S[i] == 'x' and score > 0:
            score -= 1
    return score
