def gem(N,X,Y):
    if X > Y:
        return 0
    elif X == Y:
        if N % 2 == 0:
            return (N // 2) * X
        else:
            return (N // 2) * X + 1
    else:
        if N % 2 == 0:
            return (N // 2) * (X + Y)
        else:
            return (N // 2) * (X + Y) + X
