def calc_prob(A, B, C, X):
    prob = 0
    if X <= A:
        prob = 1
    elif X <= B:
        prob = C / (B - A)
    else:
        prob = 0
    return prob
