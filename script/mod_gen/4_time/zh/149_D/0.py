def max_score(n, k, r, s, p, t):
    score = 0
    for i in range(n):
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        else:
            score += s
    return score

if __name__ == '__main__':
    max_score()