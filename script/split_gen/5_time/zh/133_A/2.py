def min_cost(N,A,B):
    if N*A > B:
        return B
    else:
        return N*A
