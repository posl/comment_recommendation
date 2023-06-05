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
        if X == A:
            return 0
        elif X == A+D:
            return 1
        else:
            return -1
    if N >= 3:
        if X == A:
            return 0
        elif (X-A)%D == 0:
            return int((X-A)/D)
        elif (X-A-D)%D == 0:
            return int((X-A-D)/D)+1
        else:
            return -1
