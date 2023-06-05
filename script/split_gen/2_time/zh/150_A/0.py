def get_max_score(N, K, R, S, P, T):
    score = 0
    for i in range(N):
        if T[i] == 'r':
            score += R
        elif T[i] == 's':
            score += S
        elif T[i] == 'p':
            score += P
    return score
