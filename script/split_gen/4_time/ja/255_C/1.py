def solve(X,A,D,N):
    if D == 0:
        if X == A:
            return 0
        else:
            return -1
    if N == 1:
        if X == A:
            return 0
        else:
            return -1
    if N == 2:
        if X == A or X == A + D:
            return 0
        else:
            return -1
    if X == A:
        return 0
    if D < 0:
        D = -D
        X = -X
        A = -A
    if X < A:
        return -1
    if (X - A) % D != 0:
        return -1
    if (X - A) // D < N - 1:
        return -1
    return (X - A) // D - (N - 1)
