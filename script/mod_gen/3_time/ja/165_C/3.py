def calc_score(A, Q, a, b, c, d):
    score = 0
    for i in range(Q):
        if A[b[i] - 1] - A[a[i] - 1] == c[i]:
            score += d[i]
    return score

if __name__ == '__main__':
    calc_score()