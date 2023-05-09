def calc_score(a, b, c, d, A):
    score = 0
    for i in range(len(a)):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            score += d[i]
    return score

if __name__ == '__main__':
    calc_score()