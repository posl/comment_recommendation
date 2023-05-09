def find_kth_greatest_value(P, K):
    P = sorted(P)
    return P[-K]
