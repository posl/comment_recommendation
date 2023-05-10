def score(a,b,c,d,seq):
    score = 0
    for i in range(len(a)):
        if seq[b[i]-1] - seq[a[i]-1] == c[i]:
            score += d[i]
    return score
