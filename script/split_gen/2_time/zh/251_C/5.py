def find_best_submission(N, S, T):
    best = -1
    best_score = -1
    for i in range(0, N):
        if S[i] == best:
            continue
        if T[i] > best_score:
            best = S[i]
            best_score = T[i]
    return best
