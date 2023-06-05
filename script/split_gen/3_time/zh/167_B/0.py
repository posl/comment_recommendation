def max_sum(A,B,C,K):
    if A >= K:
        return K
    elif A + B >= K:
        return A
    else:
        return A - (K - A - B)
