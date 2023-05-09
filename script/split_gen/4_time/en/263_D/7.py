def calc_min_sum(N, L, R, A):
    min_sum = 0
    for a in A:
        if a < 0:
            min_sum += L * a
        else:
            min_sum += R * a
    return min_sum
