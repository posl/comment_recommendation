def get_best_submission(N, S, T):
    # 1. get the best score
    # 2. get the earliest best score
    # 3. get the index of the earliest best score
    best_score = 0
    best_score_index = 0
    best_score_time = 0
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_score_index = i
            best_score_time = S[i]
        elif T[i] == best_score:
            if S[i] < best_score_time:
                best_score_index = i
                best_score_time = S[i]
    return best_score_index + 1
