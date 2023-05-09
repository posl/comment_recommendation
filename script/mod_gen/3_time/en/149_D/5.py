def calc_score(T, N, K, R, S, P):
    score = 0
    for i in range(N):
        if T[i] == 'r':
            score += P
        elif T[i] == 's':
            score += R
        elif T[i] == 'p':
            score += S
        if i >= K:
            if T[i] == T[i-K]:
                T[i] = ' '
    return score

if __name__ == '__main__':
    calc_score()