def calc_score(A, N, Q, query):
    score = 0
    for q in query:
        if A[q[1]-1] - A[q[0]-1] == q[2]:
            score += q[3]
    return score
