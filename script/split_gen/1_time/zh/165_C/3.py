def calcScore(A, Q):
    score = 0
    for i in range(len(Q)):
        if (A[Q[i][1]-1] - A[Q[i][0]-1]) == Q[i][2]:
            score += Q[i][3]
    return score
