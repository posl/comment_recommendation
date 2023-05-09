def rpsbattle(n, k, r, s, p, t):
    # print(n, k, r, s, p, t)
    # print(r, s, p)
    # print(t)
    # print(t[0])
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                score += 0
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                score += 0
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                score += 0
            else:
                score += s
    return score
