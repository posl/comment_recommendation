def score_calc(a, b, c, d):
    score = 0
    for i in range(Q):
        if a[i] < b[i]:
            score += d[i]
    return score

if __name__ == '__main__':
    score_calc()