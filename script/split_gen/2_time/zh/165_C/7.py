def get_score(n, m, q, a, b, c, d):
    score = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, q+1):
                if a[k] == i and b[k] == j:
                    score += d[k]
    return score
