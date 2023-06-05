def get_coins(A, B):
    if A >= B:
        return A + (A-1)
    else:
        return B + (B-1)
