def get_score(n, m, q, a, b, c, d):
    score = 0
    for i in range(q):
        if a[i] < b[i]:
            score += d[i]
    return score

if __name__ == '__main__':
    get_score()