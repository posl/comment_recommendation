def calc_score(A, N, Q, query):
    score = 0
    for i in range(Q):
        a = query[i][0]
        b = query[i][1]
        c = query[i][2]
        d = query[i][3]
        if A[b-1] - A[a-1] == c:
            score += d
    return score

if __name__ == '__main__':
    calc_score()