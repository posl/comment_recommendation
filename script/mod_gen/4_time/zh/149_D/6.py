def get_max_score(n, k, r, s, p, t):
    score = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                score += p
            elif t[i] == 's':
                score += r
            else:
                score += s
        else:
            if t[i] == 'r':
                if t[i-k] == 'r':
                    t[i] = 'x'
                else:
                    score += p
            elif t[i] == 's':
                if t[i-k] == 's':
                    t[i] = 'x'
                else:
                    score += r
            else:
                if t[i-k] == 'p':
                    t[i] = 'x'
                else:
                    score += s
    return score

if __name__ == '__main__':
    get_max_score()