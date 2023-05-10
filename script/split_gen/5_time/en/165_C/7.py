def cal_score(A, Q, q):
    score = 0
    for i in range(Q):
        a = q[i][0]
        b = q[i][1]
        c = q[i][2]
        d = q[i][3]
        if A[b-1] - A[a-1] == c:
            score += d
    return score
