def calc_cost(N, A, X, Y):
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y
