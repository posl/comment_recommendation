def get_max_score(n, m, q, a, b, c, d):
    score = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                for l in range(1, n + 1):
                    if i <= j <= k <= l:
                        score += d[i] + d[j] + d[k] + d[l]
    return score

if __name__ == '__main__':
    get_max_score()