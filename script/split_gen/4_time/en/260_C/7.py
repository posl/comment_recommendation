def calc(N, X, Y):
    if N == 1:
        return 0
    else:
        return (N-1)*X + (N-1)*(N-2)*Y//2
