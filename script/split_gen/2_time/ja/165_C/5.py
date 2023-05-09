def calc_score(A, N, Q, query):
    score = 0
    for i in range(Q):
        a = query[i][0] - 1
        b = query[i][1] - 1
        c = query[i][2]
        d = query[i][3]
        if (A[b] - A[a]) == c:
            score += d
    return score
