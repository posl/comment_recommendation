def max_sum_card(A,B,C,K):
    if K <= A:
        return K
    elif K <= A + B:
        return A
    else:
        return A - (K - A - B)
