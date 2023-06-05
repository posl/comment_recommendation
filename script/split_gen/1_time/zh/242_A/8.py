def get_probability(A, B, C, X):
    if X <= A:
        return 1
    elif X <= B:
        return C / (B - A)
    else:
        return 0
