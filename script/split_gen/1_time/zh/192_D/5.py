def base_n_to_10(X, n):
    out = 0
    for i in X:
        out = out * n + int(i)
    return out
