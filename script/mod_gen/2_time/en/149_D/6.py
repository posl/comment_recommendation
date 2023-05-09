def get_max_score(n, k, r, s, p, t):
    max_score = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                max_score += p
            elif t[i] == 's':
                max_score += r
            elif t[i] == 'p':
                max_score += s
        else:
            if t[i] == 'r' and t[i-k] != 'p':
                max_score += p
                t[i-k] = 'p'
            elif t[i] == 's' and t[i-k] != 'r':
                max_score += r
                t[i-k] = 'r'
            elif t[i] == 'p' and t[i-k] != 's':
                max_score += s
                t[i-k] = 's'
    return max_score

if __name__ == '__main__':
    get_max_score()